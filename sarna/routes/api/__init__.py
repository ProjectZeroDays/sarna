from flask import Blueprint
from flask_restful import Api

from sarna.core.security import csrf
from sarna.routes.api import client, assessment

blueprint = Blueprint('api', __name__)
api = Api(blueprint, decorators=[csrf.exempt])

client.init_api(api)
assessment.init_api(api)