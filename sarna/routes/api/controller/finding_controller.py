from sarna.model import FindingTemplate as FindingTemplateORM
from sarna.routes.api.models import FindingTemplate
from sarna.routes.api.models.paginated_envelop import PaginatedEnvelop  # noqa: E501


def get_findign_templates(page=None, page_size=None):  # noqa: E501
    """Get a list of finding templates

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """

    findings_query = FindingTemplateORM.query.filter()
    total_count = findings_query.count()
    findingsOrm = findings_query.limit(page_size).offset(page_size * page)
    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            FindingTemplate.from_dict(f) for f in findingsOrm
        ]
    )

    return data.to_dict()
