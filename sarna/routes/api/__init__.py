from http import HTTPStatus

from flask import Blueprint, request
from flask_restful import Resource, Api, fields, marshal_with, abort

from sarna.core.auth import current_user
from sarna.core.security import csrf
from sarna.model import User, Client

blueprint = Blueprint('api', __name__)
api = Api(blueprint, prefix='/clients', decorators=[csrf.exempt])

client_fields = {
    'id': fields.Integer,
    'short_name': fields.String,
    'long_name': fields.String,
    'creator': fields.String(attribute='creator.name'),
    'managers': fields.List(
        fields.String,
        attribute=lambda xs: list(x.name for x in xs.managers)
    ),
    'auditors': fields.List(
        fields.String,
        attribute=lambda xs: list(x.name for x in xs.auditors)
    )
}


@api.resource('/<int:id>')
class ClientApi(Resource):
    @marshal_with(client_fields, envelope='data')
    def get(self, id):
        client = Client.query.filter_by(id=id).first()

        if not client or not current_user.audits(client):
            abort(
                HTTPStatus.FORBIDDEN,
                error_code=HTTPStatus.FORBIDDEN,
                error=HTTPStatus.FORBIDDEN.phrase,
                message=HTTPStatus.FORBIDDEN.description
            )

        return client

    def delete(self, id):
        client = Client.query.filter_by(id=id).first()

        if not client or not current_user.owns(client):
            abort(
                HTTPStatus.FORBIDDEN,
                error_code=HTTPStatus.FORBIDDEN,
                error=HTTPStatus.FORBIDDEN.phrase,
                message=HTTPStatus.FORBIDDEN.description
            )

        client.delete()

        return '', 204


@api.resource('/')
class ClientListApi(Resource):
    @marshal_with(client_fields, envelope='data')
    def get(self):
        clients = Client.query.filter(
            (Client.creator == current_user) |
            (Client.managers.any(User.id == current_user.id)) |
            (Client.auditors.any(User.id == current_user.id))
        ).all()

        return clients

    def post(self):
        return request.json
