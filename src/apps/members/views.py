from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView

from apps.members.forms import NewBoardMemberForm
from apps.boards.models import Board


class NewBoardMemberView(FormView):
    template_name = 'members/new.html'
    form_class = NewBoardMemberForm

    def form_valid(self, form):
        board = self.get_board()
        chosen_user = form.cleaned_data['user']
        board.members.add(chosen_user)
        return redirect(board.get_absolute_url())

    def get_board(self):
        return get_object_or_404(Board, id=self.kwargs['board_pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['board'] = self.get_board()
        return kwargs
