import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.newsletters.models import Subscriber


@pytest.mark.django_db
def test_subscriber_list_view():
    Subscriber.objects.bulk_create([
        Subscriber(email=f'oleks{i}@gmail.com') for i in range(60)
    ])
    client = APIClient()
    resp = client.get(reverse('newsletters:subscribers'))
    assert resp.status_code == 200

    assert resp.data['count'] == 60
    assert len(resp.data['results']) == 50


@pytest.mark.django_db
def test_subscriber_create_view():
    client = APIClient()

    assert Subscriber.objects.all().count() == 0

    data = {'email': 'oleks@gmail.com'}
    resp = client.post(reverse('newsletters:subscribers'), data=data)

    assert resp.status_code == 201
    assert Subscriber.objects.all().count() == 1
    assert resp.data['email'] == 'oleks@gmail.com'

    data = {'email': 'oleks@gmail.com'}
    resp = client.post(reverse('newsletters:subscribers'), data=data)
    assert resp.status_code == 400
