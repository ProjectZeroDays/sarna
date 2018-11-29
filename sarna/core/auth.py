from flask_login import LoginManager, login_required, current_user, logout_user

from sarna.core import app
from sarna.model.user import User

__all__ = [
    'login_manager', 'logout_user', 'login_required', 'current_user'
]

login_manager = LoginManager()

login_manager.login_view = "index.index"
# login_manager.session_protection = "strong"
login_manager.login_message_category = 'success'

current_user: User = current_user


def bearer_token_info(access_token, required_scopes=None):
    return User.query.filter_by(access_token=access_token).first()


@login_manager.request_loader
def load_user_from_request(request):
    schema, *access_token = request.headers.get('Authorization', '').split(' ', maxsplit=2)
    access_token = ''.join(access_token)
    if schema == "Bearer":
        user = User.query.filter_by(access_token=access_token).first()
        if user:
            return user

    return None


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()


@app.context_processor
def processor_can_view():
    def can_view(endpoint: str):
        if current_user.is_anonymous:
            return False

        view_func = app.view_functions.get(endpoint, None)
        if view_func:
            needs = getattr(view_func, 'needs_accounts', None)
            if needs:
                return current_user.user_type in needs
        return True

    return dict(can_view=can_view)
