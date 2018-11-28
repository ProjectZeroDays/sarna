import connexion

from sarna.routes.api import encoder

_app = connexion.App(__name__, specification_dir='./swagger/', options={"swagger_ui": False})
_app.app.json_encoder = encoder.JSONEncoder
_api = _app.add_api('swagger.yaml', arguments={'title': 'SARNA API'})

blueprint = _api.blueprint
