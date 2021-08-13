import string

import factory
from factory import fuzzy

from apps.boards.models import Board, Col
from tests.factories.users import TrelloUserFactory


class BoardFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    owner = factory.SubFactory(TrelloUserFactory)

    class Meta:
        model = Board


class ColumnFactory(factory.django.DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    board = factory.SubFactory(BoardFactory)

    class Meta:
        model = Col
