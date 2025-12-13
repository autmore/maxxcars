from http import HTTPStatus

from django.http import HttpRequest

from cars.models import Car
from common.api.get_object_or_404 import get_object_or_raise_404
from rest_api.v1.cars.schemas.output import CarSchema


def get_car(
    request: HttpRequest,
    car_id: int
) -> [HTTPStatus, CarSchema]:
    car: Car = get_object_or_raise_404(Car, id=car_id)
    return HTTPStatus.OK, CarSchema.from_orm(car)
