from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class TaskManager(models.Manager):

    def new_task(self, board, **kwargs):
        return Task.objects.create(
            board=board,
            **kwargs
        )

    def set_status(self, task, status, commit=False):
        task.status = status

        if commit:
            task.save(update_field=['status'])

    def set_owner(self, task, assigned_to, commit=False):
        task.assigned_to = assigned_to

        if commit:
            task.save(update_field=['assigned_to'])


class TaskQuerySet(models.QuerySet):

    def active(self):
        return self.filter(status=Task.STATUS_ACTIVE)

    def closed(self):
        return self.filter(status=Task.STATUS_CLOSED)

    def archived(self):
        return self.filter(status=Task.STATUS_ARCHIVE)

    def by_user(self, user):
        return self.filter(assigned_to=user)

    def by_user_id(self, user_id: int):
        return self.filter(assigned_to_id=user_id)


class Task(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_CLOSED = 'closed'
    STATUS_ARCHIVE = 'archive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Активний'),
        (STATUS_CLOSED, 'Закритий'),
        (STATUS_ARCHIVE, 'Архівовано'),
    )

    assigned_to = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    board = models.ForeignKey(
        'boards.Board',
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    picture = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )

    objects = TaskManager.from_queryset(TaskQuerySet)()

    class Meta:
        verbose_name = 'Таск'
        verbose_name_plural = 'Таски'

    def __str__(self):
        return f'Task: {self.assigned_to_id}'
