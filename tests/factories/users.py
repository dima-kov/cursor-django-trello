import string

import factory
from factory import fuzzy

from apps.users.models import TrelloUser


class TrelloUserFactory(factory.django.DjangoModelFactory):
    first_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    last_name = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    username = fuzzy.FuzzyText(length=12, chars=string.ascii_letters, prefix='')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())

    class Meta:
        model = TrelloUser
