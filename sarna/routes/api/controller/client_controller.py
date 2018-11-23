import connexion
import six

from sarna.routes.api.models.envelop import Envelop  # noqa: E501
from sarna.routes.api import util


def get_client(client_id):  # noqa: E501
    """Get client data

     # noqa: E501

    :param client_id: Client ID
    :type client_id: int

    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'


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
