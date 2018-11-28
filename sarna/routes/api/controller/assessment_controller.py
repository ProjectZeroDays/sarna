from flask import abort

from sarna.core.auth import current_user
from sarna.model import Assessment as AssessmentORM
from sarna.model import Finding as FindingORM
from sarna.routes.api.models import Assessment, Finding, PaginatedEnvelop
from sarna.routes.api.models.envelop import Envelop  # noqa: E501


def get_assessment(assessment_id):  # noqa: E501
    """Get assessment data

     # noqa: E501

    :param assessment_id: Assessment ID
    :type assessment_id: int

    :rtype: None
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

    :rtype: None
    """
    assessmentOrm: AssessmentORM = AssessmentORM.query.filter_by(id=assessment_id).one()
    if not current_user.audits(assessmentOrm):
        abort(403)

    findings_query = FindingORM.query.filter_by(assessment_id=assessment_id)
    total_count = findings_query.count()
    findingsOrm = findings_query.limit(page_size).offset(page_size*page)
    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            Finding.from_dict(f) for f in findingsOrm
        ]
    )
    return data.to_dict()
