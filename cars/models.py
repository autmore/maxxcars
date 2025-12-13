from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'car'
        db_table = 'm_cars'
