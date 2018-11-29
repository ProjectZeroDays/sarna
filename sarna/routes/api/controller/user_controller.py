from sarna.model import User as UserORM
from sarna.routes.api.models import User
from sarna.routes.api.models.paginated_envelop import PaginatedEnvelop  # noqa: E501


def get_users(page=None, page_size=None):  # noqa: E501
    """Get a list of Users

     # noqa: E501

    :param page: Number of page
    :type page: int
    :param page_size: Number of items returned
    :type page_size: int

    :rtype: PaginatedEnvelop
    """
    userss_query = UserORM.query.filter()
    total_count = userss_query.count()
    usersOrm = userss_query.limit(page_size).offset(page_size * page)
    data = PaginatedEnvelop(
        total=total_count,
        page_size=page_size,
        page=page,
        data=[
            User.from_dict(f) for f in usersOrm
        ]
    )

    return data.to_dict()
