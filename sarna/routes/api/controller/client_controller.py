import connexion
from flask import abort

from sarna.core.auth import current_user
from sarna.model import Assessment as AssessmentORM
from sarna.model import Client as ClientORM
from sarna.model import User as UserORM
from sarna.routes.api.models.assessment import Assessment  # noqa: E501
from sarna.routes.api.models.client import Client  # noqa: E501
from sarna.routes.api.models.envelop import Envelop  # noqa: E501
from sarna.routes.api.models.paginated_envelop import PaginatedEnvelop  # noqa: E501


def create_assessment(client_id, assessment):  # noqa: E501
    """Create a new assessment for client

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int
    :param assessment: The assessment to create.
    :type assessment: dict | bytes

    :rtype: Envelop
    """
    if connexion.request.is_json:
        assessment = Assessment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_client(client):  # noqa: E501
    """Create a new client

     # noqa: E501

    :param client: The client to create.
    :type client: dict | bytes

    :rtype: Envelop
    """
    if connexion.request.is_json:
        client = Client.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_client(client_id):  # noqa: E501
    """Get client data

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int

    :rtype: Envelop
    """
    clientOrm: ClientORM = ClientORM.query.filter_by(id=client_id).one()
    if not current_user.audits(clientOrm):
        abort(403)

    return Envelop(data=Client(clientOrm)).to_dict()


def get_client_assessments(client_id, page=None, page_size=None):  # noqa: E501
    """Get list of assessment of the client

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int
    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """
    clientOrm: ClientORM = ClientORM.query.filter_by(id=client_id).one()
    if not current_user.audits(clientOrm):
        abort(403)

    assessments_query = AssessmentORM.query.filter_by(client_id=client_id)
    total_count = assessments_query.count()
    assessmentsOrm = assessments_query.limit(page_size).offset(page_size * page)
    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            Assessment.from_dict(a.to_dict()) for a in assessmentsOrm
        ]
    )

    return data.to_dict()


def get_client_templates(client_id, page=None, page_size=None):  # noqa: E501
    """Get list of assessment of the client

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int
    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """
    return 'do some magic!'


def get_clients(page=None, page_size=None):  # noqa: E501
    """Get a list of clients

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """
    clients_query = ClientORM.query.filter(
        (ClientORM.creator == current_user) |
        (ClientORM.managers.any(UserORM.id == current_user.id)) |
        (ClientORM.auditors.any(UserORM.id == current_user.id))
    )
    total_count = clients_query.count()
    clientsOrm = clients_query.limit(page_size).offset(page * page_size)

    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            Client.from_dict(c) for c in clientsOrm
        ]
    )

    return data.to_dict()


def modify_client(client_id, client):  # noqa: E501
    """Modify client

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int
    :param client: The client to create.
    :type client: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        client = Client.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
