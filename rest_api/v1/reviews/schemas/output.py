from ninja import Schema
from pydantic import EmailStr

from rest_api.v1.cars.schemas.output import CarSchema


class ReviewOutSchema(Schema):
    name: str
    review: str
    rating: int


class ReviewsOutSchema(Schema):
    reviews: list[ReviewOutSchema]