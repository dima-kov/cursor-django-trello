from django.urls import path

from apps.boards.views import DetailBoardView
from apps.boards.views import BoardsListView

app_name = 'boards'

urlpatterns = [
    path(
        '',
        BoardsListView.as_view(),
    ),
    path(
        '<int:board_pk>/',
        DetailBoardView.as_view(),
    ),
]
