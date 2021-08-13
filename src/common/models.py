from django.db import models

from common.managers import SoftDeleteManager
from common.querysets import SoftDeleteQuerySet


class BaseDateAuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteAuditAbstractModel(BaseDateAuditModel):
    is_active = models.BooleanField(default=True, db_index=True, null=True)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()
    # objects = models.Manager().from_queryset(SoftDeleteQuerySet)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True
