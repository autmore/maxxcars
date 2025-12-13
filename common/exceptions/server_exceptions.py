from http import HTTPStatus as status

from django.utils.encoding import force_str

from common.exceptions.base_exception import BaseAPIException


class ServerException(BaseAPIException):
    status_code = status.INTERNAL_SERVER_ERROR
    default_detail = "Сервер столкнулся с ситуацией, которую не знает как обработать"


class NotImplemented(ServerException):
    status_code = status.NOT_IMPLEMENTED
    default_detail = "Метод {method} не поддерживается сервером и не может быть обработан"

    def __init__(self, method, detail=None, schema=None):
        if detail is None:
            detail = force_str(self.default_detail).format(method=method)

        super().__init__(detail, schema)


class BadGateway(ServerException):
    status_code = status.BAD_GATEWAY
    default_detail = "Не удалось получить ответ"


class ServiceUnavailable(ServerException):
    status_code = status.SERVICE_UNAVAILABLE
    default_detail = "Сервер недоступен по причине сбоя"


class GatewayTimeout(ServerException):
    status_code = status.GATEWAY_TIMEOUT
    default_detail = "Таймаут по отдаче ответа клиенту"


class VariantAlsoNegotiates(ServerException):
    status_code = status.VARIANT_ALSO_NEGOTIATES
    default_detail = "Неверная внутрення конфигурация сервера"


class NetworkAuthenticationRequired(ServerException):
    status_code = status.NETWORK_AUTHENTICATION_REQUIRED
    default_detail = "Требуется сетевая аутентификация"
