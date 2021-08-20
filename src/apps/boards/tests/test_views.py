from django.test import TestCase

from apps.boards.tests.factories import BoardFactory
from apps.users.tests.factories import UserFactory


class BoardDetailViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_added = UserFactory()
        cls.user_not_added = UserFactory()

        cls.board = BoardFactory()
        cls.board.users.add(cls.user_added)
        cls.url = f'/boards/{cls.board.id}/'

    def test_user_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_user_not_authorized(self):
        self.client.force_login(self.user_not_added)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)

    def test_ok(self):
        self.client.force_login(self.user_added)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.board.name)

    def test_not_found(self):
        self.client.force_login(self.user_added)
        response = self.client.get('/boards/214124141/')
        self.assertEqual(response.status_code, 404)
