from common.api.pagination import GenericLimitOffsetPagination
from rest_api.v1.reviews.schemas.output import ReviewOutSchema


class ReviewPagination(GenericLimitOffsetPagination[ReviewOutSchema]): ...
