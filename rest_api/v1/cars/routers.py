from http import HTTPStatus

from ninja import Router

from common.exceptions.schemas import APIExceptionOutSchema
from common.api.schemas import BaseOutSchema
from common.api.tags import OpenApiTags, ApiSummary
from rest_api.v1.cars.api.create_car import create_car
from rest_api.v1.cars.api.get_car import get_car
from rest_api.v1.cars.api.get_cars import cars_list
from rest_api.v1.cars.schemas.output import CarsOutSchema, CarSchema
from rest_api.v1.cars.schemas.pagination import CarsPagination

router = Router(tags=[OpenApiTags.Cars])

router.add_api_operation(
    methods=["GET"],
    path="/",
    view_func=cars_list,
    response={
        HTTPStatus.OK: list[CarSchema]
    },
    summary=ApiSummary.GET_CARS,
)

router.add_api_operation(
    methods=["GET"],
    path="/{car_id}",
    view_func=get_car,
    response={
        HTTPStatus.OK: CarSchema,
        HTTPStatus.NOT_FOUND: APIExceptionOutSchema
    },
    summary=ApiSummary.GET_CAR,
)

router.add_api_operation(
    methods=["POST"],
    path="/",
    view_func=create_car,
    response={
        HTTPStatus.CREATED: BaseOutSchema,
    },
    summary=ApiSummary.CREATE_CAR,
)