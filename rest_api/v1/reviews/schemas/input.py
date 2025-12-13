from ninja import Schema


class ReviewInSchema(Schema):
    name: str
    review: str
    rating: int

