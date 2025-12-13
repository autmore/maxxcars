from ninja import Schema


class CarSchema(Schema):
    name: str
    price: float


class CarsOutSchema(Schema):
    cars: list[CarSchema]
