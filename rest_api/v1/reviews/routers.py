from http import HTTPStatus

from ninja import Router

from common.api.schemas import BaseOutSchema
from common.api.tags import OpenApiTags, ApiSummary

from rest_api.v1.reviews.api.create_review import create_review
from rest_api.v1.reviews.api.review_list import review_list
from rest_api.v1.reviews.schemas.output import ReviewsOutSchema

router = Router(tags=[OpenApiTags.Reviews])

router.add_api_operation(
    methods=["GET"],
    path="/",
    view_func=review_list,
    response={
        HTTPStatus.OK: list[ReviewsOutSchema]
    },
    summary=ApiSummary.GET_REVIEWS,
)

router.add_api_operation(
    methods=["POST"],
    path="/",
    view_func=create_review,
    response={
        HTTPStatus.CREATED: BaseOutSchema,
    },
    summary=ApiSummary.CREATE_REVIEW,
)