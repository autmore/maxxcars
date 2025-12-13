from http import HTTPStatus as status

from django.http import HttpResponseNotFound
from django.utils.encoding import force_str
from ninja import Schema

from common.exceptions.base_exception import BaseAPIException


class ClientException(BaseAPIException):
    status_code = status.BAD_REQUEST
    default_detail = "Клиент столкнулся с ситуацией, которую не знает как обработать"


class ConflictException(ClientException):
    status_code = status.CONFLICT
    default_detail = "Конфликт"


class ParseError(ClientException):
    default_detail = "Неправильный, некорректный запрос"


class AuthenticationFailed(ClientException):
    status_code = status.UNAUTHORIZED
    default_detail = "Неправильные учетные данные для аутентификации"



class NotAuthenticated(ClientException):
    status_code = status.UNAUTHORIZED
    default_detail = "Учетные данные не были предоставлены"


class PermissionDenied(ClientException):
    status_code = status.FORBIDDEN
    default_detail = "У вас нет разрешения на выполнение этого действия"


class AdminPermissionDenied(PermissionDenied):
    default_detail = "Для выполнения этого действия необходимо разлогиниться в админке"


class NotFound(ClientException):
    status_code = status.NOT_FOUND
    default_detail = "Не найдено"


class EmptyNotFound(NotFound):
    def generate_exception_response(self) -> HttpResponseNotFound:
        return HttpResponseNotFound(status=self.status_code)


class MethodNotAllowed(ClientException):
    status_code = status.METHOD_NOT_ALLOWED
    default_detail = "Метод '{method}' не разрешен"

    def __init__(self, method, detail: str | None = None, schema: Schema | None = None):
        if detail is None:
            detail = force_str(self.default_detail).format(method=method)

        super().__init__(detail, schema)


class NotAcceptable(ClientException):
    status_code = status.NOT_ACCEPTABLE
    default_detail = "Не удалось удовлетворить заголовок Accept запроса"


class UnsupportedMediaType(ClientException):
    status_code = status.UNSUPPORTED_MEDIA_TYPE
    default_detail = "Неподдерживаемый тип мультимедиа '{media_type}' в запросе"

    def __init__(self, media_type, detail: str | None = None, schema: Schema | None = None):
        if detail is None:
            detail = force_str(self.default_detail).format(media_type=media_type)

        super().__init__(detail, schema)


class ValidationError(ClientException):
    status_code = status.UNPROCESSABLE_ENTITY
    default_detail = "Некорректные входные данные"


class Throttled(ClientException):
    status_code = status.TOO_MANY_REQUESTS
    default_detail = "Слишком много запросов"
