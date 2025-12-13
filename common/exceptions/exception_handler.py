import logging

from django.http import HttpRequest
from ninja import NinjaAPI

from common.exceptions.base_exception import BaseAPIException, ResponseType

logger = logging.getLogger(__name__)


def add_exceptions_handler(router: NinjaAPI):
    @router.exception_handler(BaseAPIException)
    def through_exception(request: HttpRequest, exc) -> ResponseType:
        logger.exception(exc.__repr__())
        return exc.generate_exception_response()
