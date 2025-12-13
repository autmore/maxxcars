from ninja import FilterSchema, Field


class OrdersFilterSchema(FilterSchema):
    search: str = Field(
        None,
        json_schema_extra={
            "q": [
                "name__icontains",
                "email__icontains",
                "phone_number__icontains",
                "car__name__icontains",
            ]
        },
        description="Поиск по имени пользователя, почте, номеру телефона и названию машины",
    )
