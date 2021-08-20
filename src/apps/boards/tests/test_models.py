import pytest

from django.db import IntegrityError
from django.test import TestCase

from apps.boards.models import Board
from apps.users.tests.factories import UserFactory

from apps.boards.models import Task


@pytest.mark.django_db
def test_board_model():
    """
    Test unique together for Board model
    """
    user_1 = UserFactory()
    unique_name = 'some_unique_name'
    board = Board.objects.create(
        name=unique_name,
        owner=user_1
    )
    assert board.id is not None

    with pytest.raises(IntegrityError):
        Board.objects.create(
            name=unique_name,
            owner=user_1,
        )


class TestTaskModel(TestCase):

    def setUp(self) -> None:
        self.user = UserFactory()

    def test_model(self):
        task = Task.objects.create(
            name='fake task',
            created_by=self.user,
            description='some long description',
        )

        self.assertIsNotNone(task.id)
        self.assertEqual(str(task), 'fake task')
        self.assertEqual(task.status, Task.STATUS_OPEN)

    def test_task_delete(self):
        task = Task.objects.create(
            name='fake task',
            created_by=self.user,
            description='some long description',
        )

        task.delete()
        self.assertEqual(task.status, Task.STATUS_ARCHIVED)
