from typing import Any, NoReturn, Type

from django.db.models import Model

from common.exceptions.client_exceptions import NotFound


def get_object_or_raise_404(model: Type[Model], **kwargs: Any) -> Model | NoReturn:
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise NotFound(
            detail="В {model} отсутствуют записи по запросу.".format(model=model._meta.object_name)
        )
