
from django.test import TestCase

from apps.boards.models import Task
from apps.users.tests.factories import UserFactory
from apps.boards.service import delete_task
from apps.boards.service import ProtectedTaskDelete


class ServiceTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            name='fake task',
            created_by=UserFactory(),
            description='some long description',
        )

    def test_protected(self):
        self.task.protected = True

        with self.assertRaises(ProtectedTaskDelete):
            delete_task(self.task)
