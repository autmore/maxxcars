from http import HTTPStatus
from typing import Any

from django.http import HttpRequest

from common.api.get_object_or_404 import get_object_or_raise_404
from cars.models import Car
from common.api.schemas import BaseOutSchema
from orders.models import Order
from rest_api.v1.orders.schemas.input import OrderInSchema


def create_order(
    request: HttpRequest,
    payload: OrderInSchema
) -> [HTTPStatus.CREATED, BaseOutSchema]:
    order_dict: dict[str, Any] = payload.model_dump(include={"name", "phone_number", "email"})
    order_dict.update(
        {"car_id": get_object_or_raise_404(Car, id=payload.car_id)}
    )
    new_order: Order = Order(**order_dict)
    new_order.save()
    return HTTPStatus.CREATED, BaseOutSchema(id=new_order.id)
