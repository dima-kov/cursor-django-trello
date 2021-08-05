from django.urls import path

from apps.members import views

urlpatterns = [
    path(
        'new/',
        views.NewBoardMemberView.as_view(),
    )
]
