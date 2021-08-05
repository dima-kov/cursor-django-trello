from django import forms
from django.contrib.auth.models import User

from apps.boards.models import Board


class NewBoardMemberForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Вибери юзера"
    )

    def __init__(self, board: Board, *args, **kwargs):
        self.board = board
        super().__init__(*args, **kwargs)

        board_members_ids = self.board.members.all().values_list('id', flat=True)
        self.fields['user'].queryset = User.objects.exclude(id__in=board_members_ids)
