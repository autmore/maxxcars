from django.db import models

from reviews.enum import Rating


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    review = models.TextField(null=False)
    rating = models.IntegerField(null=False, choices=Rating)

    class Meta:
        verbose_name = 'review'
        db_table = 'm_reviews'
