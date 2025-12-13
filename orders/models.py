from django.db import models

from cars.models import Car
from common.api.models import TimeStampMixin


class Order(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    car = models.ForeignKey(Car, null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'order'
        db_table = 'm_orders'
