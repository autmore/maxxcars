from ninja import Schema


class APIExceptionOutSchema(Schema):
    detail: str
