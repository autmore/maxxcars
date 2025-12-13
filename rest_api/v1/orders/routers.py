from http import HTTPStatus

from ninja import Router

from common.exceptions.schemas import APIExceptionOutSchema
from common.api.schemas import BaseOutSchema
from common.api.tags import OpenApiTags, ApiSummary
from rest_api.v1.orders.api.create_order import create_order
from rest_api.v1.orders.api.order_list import order_list
from rest_api.v1.orders.schemas.output import OrderOutSchema

router = Router(tags=[OpenApiTags.Orders])

router.add_api_operation(
    methods=["GET"],
    path="/",
    view_func=order_list,
    response={
        HTTPStatus.OK: list[OrderOutSchema]
    },
    summary=ApiSummary.GET_ORDERS,
)

router.add_api_operation(
    methods=["POST"],
    path="/",
    view_func=create_order,
    response={
        HTTPStatus.CREATED: BaseOutSchema,
    },
    summary=ApiSummary.CREATE_ORDER,
)