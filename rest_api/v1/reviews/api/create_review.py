from http import HTTPStatus

from django.http import HttpRequest

from common.api.schemas import BaseOutSchema
from rest_api.v1.reviews.schemas.input import ReviewInSchema
from reviews.models import Reviews


def create_review(
    request: HttpRequest,
    payload: ReviewInSchema
) -> [HTTPStatus.CREATED, BaseOutSchema]:
    review: Reviews = Reviews(**payload.model_dump())
    review.save()
    return HTTPStatus.CREATED, BaseOutSchema(id=review.id)
