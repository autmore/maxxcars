from datetime import timezone

from django.db import models
from django.utils import timezone


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created at')
    updated_at = models.DateTimeField(null=True, editable=False, verbose_name='updated at')

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
