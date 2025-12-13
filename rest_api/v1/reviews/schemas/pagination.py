from common.api.pagination import GenericLimitOffsetPagination
from rest_api.v1.orders.schemas.output import OrdersOutSchema
from rest_api.v1.reviews.schemas.output import ReviewsOutSchema


class ReviewPagination(GenericLimitOffsetPagination[ReviewsOutSchema]): ...