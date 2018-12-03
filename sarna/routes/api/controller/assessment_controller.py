import connexion
from flask import abort

from sarna.core.auth import current_user
from sarna.model import Assessment as AssessmentORM
from sarna.model import Finding as FindingORM
from sarna.routes.api.models import FindingRequestBody
from sarna.routes.api.models.assessment import Assessment
from sarna.routes.api.models.envelop import Envelop  # noqa: E501
from sarna.routes.api.models.finding import Finding
from sarna.routes.api.models.paginated_envelop import PaginatedEnvelop  # noqa: E501
from sarna.routes.api import util


def add_assessment_finding(assessment_id, finding_request_body):  # noqa: E501
    """Add a new finding to the assessment

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int
    :param finding_request_body: The finding to be created.
    :type finding_request_body: dict | bytes

    :rtype: Envelop
    """
    if connexion.request.is_json:
        finding_request_body = FindingRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_assessment_image(assessment_id):  # noqa: E501
    """Add evidence to assessment

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_assessment(assessment_id):  # noqa: E501
    """Delete Assessment

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_assessment_finding(assessment_id, finding_id):  # noqa: E501
    """Delete Assessment Finding

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int
    :param finding_id: Finding ID
    :type finding_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_assessment_image(assessment_id, filename):  # noqa: E501
    """Delete Assessment image

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int
    :param filename: Filename
    :type filename: str

    :rtype: None
    """
    return 'do some magic!'


def delete_finding_template(finding_id):  # noqa: E501
    """Delete Finding Template

     # noqa: E501

    :param finding_id: Finding ID
    :type finding_id: int

    :rtype: None
    """
    return 'do some magic!'


def edit_assessment_finding(assessment_id, finding_id, finding_request_body):  # noqa: E501
    """Edit finding in the assessment

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int
    :param finding_id: Finding ID
    :type finding_id: int
    :param finding_request_body: The finding to be edited.
    :type finding_request_body: dict | bytes

    :rtype: Envelop
    """
    if connexion.request.is_json:
        finding_request_body = FindingRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_assessment(assessment_id):  # noqa: E501
    """Get assessment data

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int

    :rtype: Envelop
    """
    assessmentOrm: AssessmentORM = AssessmentORM.query.filter_by(id=assessment_id).one()
    if not current_user.audits(assessmentOrm):
        abort(403)

    return Envelop(data=Assessment.from_dict(assessmentOrm)).to_dict()


def get_assessment_findingis(assessment_id, page=None, page_size=None):  # noqa: E501
    """Get a list of findings in assessment

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int
    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """
    assessmentOrm: AssessmentORM = AssessmentORM.query.filter_by(id=assessment_id).one()
    if not current_user.audits(assessmentOrm):
        abort(403)

    findings_query = FindingORM.query.filter_by(assessment_id=assessment_id)
    total_count = findings_query.count()
    findingsOrm = findings_query.limit(page_size).offset(page_size * page)
    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            Finding.from_dict(f) for f in findingsOrm
        ]
    )
    return data.to_dict()

def get_assessment_image(assessment_id, filename):  # noqa: E501
    """Download assessment image

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int
    :param filename: Filename
    :type filename: str

    :rtype: file
    """
    return 'do some magic!'


def get_assessment_images(assessment_id):  # noqa: E501
    """Get list of images

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int

    :rtype: PaginatedEnvelop
    """
    return 'do some magic!'


def get_assessments(page=None, page_size=None):  # noqa: E501
    """Get a list of assessments

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """

    assessments_query = current_user.get_user_assessments()
    total_count = assessments_query.count()
    assessment_orm = assessments_query.limit(page_size).offset(page_size * page)
    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            Assessment.from_dict(f) for f in assessment_orm
        ]
    )

    return data.to_dict()
