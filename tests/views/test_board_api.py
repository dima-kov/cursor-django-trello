import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from tests.factories.boards import BoardFactory, ColumnFactory


class TestBoardApi:
    client = APIClient()

    @pytest.mark.django_db
    def test_change_ordering(self):
        board = BoardFactory()
        col1 = ColumnFactory(board=board, position=0)
        col2 = ColumnFactory(board=board, position=1)

        data = {
            'columns': [
                {'id': col1.id, 'position': 1},
                {'id': col2.id, 'position': 0}
            ]
        }
        resp = self.client.patch(reverse('bb:boards-change-task-ordering'), data=data)

        assert resp.status_code == 200
        assert resp.data['columns'] == data['columns']

        col1.refresh_from_db()
        col2.refresh_from_db()
        assert col1.position == 1
        assert col2.position == 0
