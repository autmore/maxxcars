from ninja import Schema
from pydantic import EmailStr

from rest_api.v1.cars.schemas.output import CarSchema


class OrderOutSchema(Schema):
    name: str
    phone_number: str
    email: EmailStr
    car: CarSchema

    model_config = {
        "from_attributes": True
    }


class OrdersOutSchema(Schema):
    orders: list[OrderOutSchema]