from django import forms

from apps.boards.models import Board


class BoardEditForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = ('name', 'description')
        fields = '__all__'
