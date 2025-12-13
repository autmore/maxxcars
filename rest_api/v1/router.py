from ninja import NinjaAPI
from rest_api.v1.cars.routers import router as cars_router
from rest_api.v1.orders.routers import router as orders_router
from rest_api.v1.reviews.routers import router as review_router

api_v1 = NinjaAPI(
    version="1.0",
    title="MaxCars REST-API",
)

api_v1.add_router("cars", cars_router)
api_v1.add_router("orders", orders_router)
api_v1.add_router("reviews", review_router)
