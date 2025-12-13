from ninja import Schema


class CarInSchema(Schema):
    name: str
    price: float