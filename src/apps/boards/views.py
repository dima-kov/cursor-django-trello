from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from apps.boards.models import Board
from django.views import View
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, ListView


class BoardTemplateView(TemplateView):
    template_name = 'index.html'


class BoardRedirectTemplateView(RedirectView):
    url = '/'


class NewBoardView(CreateView):
    model = Board


def boards(request):
    boards = Board.objects.filter(owner=request.user)
    return render(
        request,
        'boards/list.html',
        {'boards': boards}
    )


class BoardsListView(ListView):
    model = Board.objects.filter()
    context_object_name = 'boards'
    template_name = 'boards/list.html'

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)


class DetailBoardView(DetailView):
    model = Board
    pk_url_kwarg = 'board_pk'
    template_name = 'boards/detail.html'
    context_object_name = 'board'


def detail_board(request, board_pk):
    board = get_object_or_404(Board, id=board_pk)
    return render(
        request,
        'boards/detail.html',
        {'board': board}
    )
