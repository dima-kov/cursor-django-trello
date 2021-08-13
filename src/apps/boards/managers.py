from django.db import models
from django.db.models import Prefetch, Q

from apps.boards.models import Task
from apps.users.models import TrelloUser


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('comments').all()


class BoardManager(models.Manager):
    def list_qs(self, user: TrelloUser):
        queryset = self.get_queryset()
        col_tasks_pref = Prefetch(
            'cols__tasks', Task.objects.select_related('created_by')
        )
        collection_lookups = Q(users__in=(self.request.user,)) | Q(owner=self.request.user)
        return queryset.filter(collection_lookups).prefetch_related(col_tasks_pref)
