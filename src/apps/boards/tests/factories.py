import factory.django

from apps.boards.models import Board


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    def __new__(cls, *args, **kwargs) -> Board:
        return super().__new__(*args, **kwargs)
