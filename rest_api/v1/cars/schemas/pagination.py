from common.api.pagination import GenericLimitOffsetPagination
from rest_api.v1.cars.schemas.output import CarsOutSchema


class CarsPagination(GenericLimitOffsetPagination[CarsOutSchema]): ...