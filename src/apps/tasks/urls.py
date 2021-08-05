from django.urls import path, include

from apps.tasks import views

task_id_patterns = [
    path(
        '',
        views.DetailTaskView.as_view(),
    ),
    # path(
    #     'edit/',
    #     EditTaskView.as_view(),
    # ),
    # path(
    #     'delete/',
    #     DeleteTaskView.as_view(),
    # ),
]

urlpatterns = [
    path(
        'board/<int:board_pk>/task/<int:task_pk>/',
        include(task_id_patterns)
    ),
    path(
        'board/<int:board_pk>/task/new/',
        views.TaskCreateView.as_view(),
    )
]
