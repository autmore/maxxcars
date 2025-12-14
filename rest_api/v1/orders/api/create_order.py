from http import HTTPStatus
from typing import Any

from django.http import HttpRequest

from common.api.get_object_or_404 import get_object_or_raise_404
from cars.models import Car
from common.api.schemas import BaseOutSchema
from common.telegram.send_message import send_telegram_message
from orders.models import Order
from rest_api.v1.orders.schemas.input import OrderInSchema


def create_order(
    request: HttpRequest,
    payload: OrderInSchema
) -> [HTTPStatus.CREATED, BaseOutSchema]:
    car: Car = get_object_or_raise_404(Car, id=payload.car_id)

    order_dict: dict[str, Any] = payload.model_dump(include={"name", "phone_number", "email"})
    order_dict["car"] = car

    new_order: Order = Order.objects.create(**order_dict)
    new_order.save()

    message = (
        "🆕 <b>Новый заказ</b>\n\n"
        f"👤 Имя: {new_order.name}\n"
        f"📞 Телефон: {new_order.phone_number}\n"
        f"📧 Email: {new_order.email}\n"
        f"🚗 Авто: {new_order.car.name}\n"
        f"💰 Цена: {new_order.car.price}$\n"
        f"🆔 ID заказа: {new_order.id}"
    )

    send_telegram_message(message)

    return HTTPStatus.CREATED, BaseOutSchema(id=new_order.id)
