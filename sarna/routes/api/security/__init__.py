from sarna.model import User


def api_key_info(api_key, required_scopes):
    user = User.query.filter_by(access_token=api_key).one()
    user.login()
    return user
