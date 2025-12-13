from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate
from rest_api.v1.reviews.schemas.filters import ReviewFilterSchema
from rest_api.v1.reviews.schemas.pagination import ReviewPagination
from reviews.models import Reviews


@paginate(ReviewPagination)
def review_list(
    request: HttpRequest,
    filters: ReviewFilterSchema = Query(),
) -> QuerySet:
    return filters.filter(Reviews.objects.all())
