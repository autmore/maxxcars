from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate

from orders.models import Order
from rest_api.v1.orders.schemas.filters import OrdersFilterSchema
from rest_api.v1.orders.schemas.pagination import OrdersPagination


@paginate(OrdersPagination)
def order_list(
    request: HttpRequest,
    filters: OrdersFilterSchema = Query(),
) -> QuerySet:
    return filters.filter(Order.objects.select_related('car').all())
