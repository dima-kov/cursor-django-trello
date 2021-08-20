from collections import OrderedDict

from django.test import TestCase
from rest_framework.test import APIClient

from apps.boards.tests.factories import BoardFactory
from apps.users.tests.factories import UserFactory, USER_FACTORY_PASSWORD


class BoardListCreateViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_added = UserFactory()
        cls.user_not_added = UserFactory()

        cls.board = BoardFactory()
        cls.board.users.add(cls.user_added)
        cls.url = f'/boards/'

    def setUp(self) -> None:
        self.rest_client = APIClient()

    def test_user_not_authenticated(self):
        response = self.rest_client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_user_not_authorized(self):
        self.rest_client.login(
            username=self.user_not_added.username,
            password=USER_FACTORY_PASSWORD
        )
        response = self.rest_client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.assertTrue(isinstance(response.data, OrderedDict))
        self.assertEqual(response.data['count'], 0)

    def test_ok(self):
        self.rest_client.login(
            username=self.user_added.username,
            password=USER_FACTORY_PASSWORD
        )
        response = self.rest_client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.assertTrue(isinstance(response.data, OrderedDict))
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['id'], self.board.id)
