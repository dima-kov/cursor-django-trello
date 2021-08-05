from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic as views

from apps.boards.forms import BoardEditForm
from apps.boards.models import Board


class BoardsListView(LoginRequiredMixin, views.ListView):
    model = Board.objects.filter()
    context_object_name = 'boards'
    template_name = 'boards/list.html'

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)


class DetailBoardView(LoginRequiredMixin, views.DetailView):
    model = Board
    pk_url_kwarg = 'board_pk'
    template_name = 'boards/detail.html'
    context_object_name = 'board'

    def dispatch(self, request, *args, **kwargs):
        board = self.get_object()
        if request.user.is_authenticated and board.owner_id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/board/')


class BoardCreateView(LoginRequiredMixin, views.CreateView):
    model = Board
    template_name = 'boards/new.html'
    fields = ['name', 'description']
    login_url = '/admin/login/'

    def form_valid(self, form):
        obj: Board = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return redirect('/')


class BoardEditView(LoginRequiredMixin, views.UpdateView):
    model = Board
    form_class = BoardEditForm
    template_name = 'boards/edit.html'
    pk_url_kwarg = 'board_pk'

    def dispatch(self, request, *args, **kwargs):
        board = self.get_object()
        if request.user.is_authenticated and board.owner_id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/board/')
