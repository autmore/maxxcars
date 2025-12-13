from http import HTTPStatus

from django.http import HttpRequest

from cars.models import Car
from common.api.schemas import BaseOutSchema
from rest_api.v1.cars.schemas.input import CarInSchema


def create_car(
    request: HttpRequest,
    payload: CarInSchema
) -> [HTTPStatus.CREATED, BaseOutSchema]:
    new_car = Car(**payload.model_dump())
    new_car.save()
    return HTTPStatus.CREATED, BaseOutSchema(id=new_car.id)