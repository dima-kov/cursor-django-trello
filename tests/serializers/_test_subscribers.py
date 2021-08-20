import pytest

from apps.newsletters.models import Subscriber
from apps.newsletters.serializers import SubscriberSerializer


@pytest.mark.django_db
def test_subscriber_serializer_validation():
    data = {"email": 'oleks@gmail.com'}
    serializer = SubscriberSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()

    data = {"email": 'oleks@gmail.com'}
    serializer = SubscriberSerializer(data=data)
    assert not serializer.is_valid()


@pytest.mark.django_db
def test_reversed_email_field():
    obj = Subscriber(email='oleks@gmail.com')
    serializer = SubscriberSerializer(instance=obj)

    assert serializer.data['reversed_email'] == 'oleks@gmail.com'[::-1]
