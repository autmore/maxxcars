from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import Any

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.utils.encoding import force_str
from ninja import Schema

from common.exceptions.schemas import APIExceptionOutSchema

ResponseType = JsonResponse | HttpResponseNotFound | HttpResponseBadRequest


class IApiException(ABC):
    """
    Интерфейс для кастомных исключений которые возвращаются в response.

    Аттрибуты:
    - status_code (HTTPStatus): Код статуса HTTP, связанный с исключением.
    - default_detail (str): Подробное сообщение по умолчанию для исключения.
    - schema (Schema): Django Ninja схема для исключения.
    """

    @abstractmethod
    def generate_exception_response(self) -> ResponseType:
        pass

    @abstractmethod
    def _get_detail_by_schema(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def _get_default_response_data(self) -> dict[str, Any]:
        pass


class BaseAPIException(Exception, IApiException):
    status_code: HTTPStatus
    default_detail: str
    schema: Schema | None

    def __init__(self, detail: str | None = None, schema: Schema | None = None):
        self.detail = detail if detail else self.default_detail
        self.schema = schema if schema else None

    def __repr__(self, *args, **kwargs):
        schema_name = self.schema.__class__.__name__ if self.schema else "Not set"

        return "%s: %s. Schema: %s." % (
            self.__class__.__name__,
            self.detail,
            schema_name,
        )

    def generate_exception_response(self) -> JsonResponse:
        detail: dict[str, Any] = self._get_detail_by_schema()
        return JsonResponse(data=detail, status=self.status_code)

    def _get_detail_by_schema(self) -> dict[str, Any]:
        detail: dict[str, Any] = (
            self.schema.dict() if self.schema else self._get_default_response_data()
        )
        return detail

    def _get_default_response_data(self) -> dict[str, Any]:
        decoded_str: str = force_str(self.detail)
        return APIExceptionOutSchema(detail=decoded_str).model_dump()
