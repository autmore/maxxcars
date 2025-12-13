from ninja import Schema
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class OrderInSchema(Schema):
    name: str
    phone_number: PhoneNumber
    email: EmailStr
    car_id: int

