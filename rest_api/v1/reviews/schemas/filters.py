from ninja import FilterSchema, Field


class ReviewFilterSchema(FilterSchema):
    search: str = Field(
        None,
        json_schema_extra={
            "q": [
                "name__icontains",
                "review__icontains",
            ]
        },
        description="Поиск по имени пользователя и комментарию",
    )
