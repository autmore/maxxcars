from enum import StrEnum


class OpenApiTags(StrEnum):
    Cars = "сars"
    Orders = "orders"
    Reviews = "reviews"


class ApiSummary(StrEnum):
    GET_CARS = "Получение списка всех машин"
    GET_CAR = "Получение одной машины"
    CREATE_CAR = "Запись новой машины"
    GET_ORDERS = "Получение списка заказов"
    CREATE_ORDER = "Создание нового заказа"
    GET_REVIEWS = "Получение списка отзывов"
    CREATE_REVIEW = "Создание нового отзыва"