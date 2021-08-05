from django.shortcuts import redirect, get_object_or_404
from django.views import generic as views

from apps.tasks.models import Task
from apps.boards.models import Board


class DetailTaskView(views.DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    pk_url_kwarg = 'task_pk'
    context_object_name = 'task'


class TaskCreateView(views.CreateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'tasks/new.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.board = self.get_board()
        obj.assigned_to = self.request.user
        obj.save()
        return redirect(obj.get_absolute_url())

    def get_board(self):
        return get_object_or_404(Board, id=self.kwargs['board_pk'])
