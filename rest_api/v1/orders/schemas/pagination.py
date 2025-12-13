from common.api.pagination import GenericLimitOffsetPagination
from rest_api.v1.orders.schemas.output import OrdersOutSchema


class OrdersPagination(GenericLimitOffsetPagination[OrdersOutSchema]): ...