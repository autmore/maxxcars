from ninja import FilterSchema, Field


class CarsFilterSchema(FilterSchema):
    search: str = Field(
        None,
        json_schema_extra={
            "q": [
                "name__icontains",
            ]
        },
        description="Поиск по названию",
    )
    price_min: float = Field(
        None,
        json_schema_extra={
            "q": ["price__gte"],
        },
        description="Минимальная цена машины",
    )
    price_max: float = Field(
        None,
        json_schema_extra={
            "q": ["price__lte"],
        },
        description="Максимальная цена машины",
    )
