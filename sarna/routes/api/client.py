from http import HTTPStatus

from flask import request
from flask_restful import Resource, fields, marshal_with, abort, Api

from sarna.core.auth import current_user
from sarna.model import User, Client


def init_api(api: Api):
    api.add_resource(ClientListApi, '/clients/')
    api.add_resource(ClientApi, '/clients/<int:id>')


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
