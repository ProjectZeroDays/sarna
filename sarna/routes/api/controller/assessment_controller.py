import connexion
import six

from sarna.routes.api.models.envelop import Envelop  # noqa: E501
from sarna.routes.api import util


def get_assessment(assessment_id):  # noqa: E501
    """Get assessment data

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_assessment_findingis(page=None, page_size=None):  # noqa: E501
    """Get a list of findings in assessment

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: None
    """
    return 'do some magic!'
