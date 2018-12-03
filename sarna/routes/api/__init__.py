import connexion
from flask import Blueprint

from sarna.core.security import csrf as _csrf
from sarna.routes.api import encoder

_options = {"swagger_ui": False}
_app = connexion.App(__name__, specification_dir='./openapi/', options=_options)
_app.app.json_encoder = encoder.JSONEncoder
_api = _app.add_api('openapi.yaml', arguments={'title': 'SARNA API'})

_csrf.exempt(_api.blueprint)

blueprint: Blueprint = _api.blueprint
