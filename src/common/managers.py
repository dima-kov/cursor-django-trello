from django.db import models


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(is_active=True)

    def deleted(self):
        return self.get_queryset().filter(is_active=False)
