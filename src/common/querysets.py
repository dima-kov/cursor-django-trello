from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        """Soft delete objects"""
        return self.update(is_active=False)

    def hard_delete(self):
        """Remove objects from DB"""
        return super().delete()
