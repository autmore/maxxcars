from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate

from cars.models import Car
from rest_api.v1.cars.schemas.filters import CarsFilterSchema
from rest_api.v1.cars.schemas.pagination import CarsPagination


@paginate(CarsPagination)
def cars_list(
    request: HttpRequest,
    filters: CarsFilterSchema = Query(),
) -> QuerySet:
    return filters.filter(Car.objects.all())
