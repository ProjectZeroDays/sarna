from sarna.core.auth import current_user
from sarna.model import Client as ClientORM
from sarna.model import User as UserORM
from sarna.routes.api.models import PaginatedEnvelop
from sarna.routes.api.models.client import Client
from sarna.routes.api.models.envelop import Envelop  # noqa: E501


def get_client(client_id):  # noqa: E501
    """Get client data

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int

    :rtype: None
    """
    clientOrm: ClientORM = ClientORM.query.filter_by(id=client_id).one()
    client: Client = Client.from_dict(clientOrm)
    data = Envelop(data=client)

    return data.to_dict()


def get_client_assessments(client_id, page=None, page_size=None):  # noqa: E501
    """Get list of assessment of the client

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int
    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: None
    """
    return 'do some magic!'


def get_client_templates(client_id, page=None, page_size=None):  # noqa: E501
    """Get list of assessment of the client

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int
    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: None
    """
    return 'do some magic!'


def get_clients(page=None, page_size=None):  # noqa: E501
    """Get a list of clients

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: None
    """
    clients_query = ClientORM.query.filter(
        (ClientORM.creator == current_user) |
        (ClientORM.managers.any(UserORM.id == current_user.id)) |
        (ClientORM.auditors.any(UserORM.id == current_user.id))
    )
    total_count = clients_query.count()
    clientsOrm = clients_query.limit(page_size).offset(page*page_size)

    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            Client.from_dict(c.to_dict()) for c in clientsOrm
        ]
    )

    return data.to_dict()


def get_users(page=None, page_size=None):  # noqa: E501
    """Get a list of Users

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: None
    """
    return 'do some magic!'
