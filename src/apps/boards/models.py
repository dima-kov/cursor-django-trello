from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class BoardQuerySet(models.QuerySet):

    def annotate_tasks_count(self):
        return self.annotate(tasks_count=models.Count('tasks'))

    def aggregate_tasks_count(self):
        return self.aggregate(tasks_count=models.Count('tasks'))


class Board(models.Model):
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='boards',
    )
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    members = models.ManyToManyField(
        USER_MODEL,
    )

    objects = BoardQuerySet.as_manager()

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

    def __str__(self):
        return f'{self.owner_id}: {self.name}'

    def get_absolute_url(self):
        return f'/board/{self.id}/'
