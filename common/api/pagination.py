from typing import Any, Generic, TypeVar

from django.db.models import QuerySet
from ninja import Field, Schema
from ninja.pagination import LimitOffsetPagination

from AnyaProject import settings

ItemOutSchema = TypeVar("ItemOutSchema", bound=Schema)


class GenericLimitOffsetPagination(LimitOffsetPagination, Generic[ItemOutSchema]):
    class Input(Schema):
        limit: int = Field(settings.PAGINATION_PER_PAGE, ge=1, le=100)
        offset: int = Field(0, ge=0)

    class Output(Schema):
        next_page: bool
        results: list[ItemOutSchema]
        count: int

    items_attribute: str = "results"

    def paginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> Any:

        attributes: dict[str, Any] = super().paginate_queryset(queryset, pagination, **params)
        return {
            "next_page": pagination.offset + pagination.limit < attributes["count"],
            "results": attributes["results"],
            "count": attributes["count"],
        }
