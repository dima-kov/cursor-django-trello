from django.urls import path

from apps.boards import views

app_name = 'boards'

urlpatterns = [
    path(
        '',
        views.BoardsListView.as_view(),
    ),
    path(
        'new/',
        views.BoardCreateView.as_view(),
    ),
    path(
        '<int:board_pk>/',
        views.DetailBoardView.as_view(),
    ),
    path(
        '<int:board_pk>/edit/',
        views.BoardEditView.as_view(),
    ),
]
