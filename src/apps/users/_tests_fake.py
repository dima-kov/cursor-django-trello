# Create your tests here.
import pytest
from django.test import Client
from django.urls import reverse

from apps.users.forms import LoginForm
from apps.users.models import TrelloUser
from tests.factories.users import TrelloUserFactory


def create_test_user(**fields) -> TrelloUser:
    ## TODO move to fixture
    username = fields.get("username", 'test_user')
    password = fields.get('password', "Super$ecretPa$$word")
    test_user = TrelloUserFactory(username=username)
    test_user.set_password(password)
    test_user.save()
    return test_user


@pytest.mark.django_db
def test_login_form():
    username = 'test_user'
    password = "Super$ecretPa$$word"
    test_user = create_test_user(username=username, password=password)

    data = {
        "password": password,
        "username": username
    }
    form = LoginForm(data=data)

    assert form.is_valid()
    assert 'user' in form.cleaned_data
    assert form.cleaned_data['user'].id == test_user.id


@pytest.mark.django_db
def test_login_view():
    username = 'test_user'
    password = "Super$ecretPa$$word"
    create_test_user(username=username, password=password)

    url = reverse('users:login-page')
    data = {'username': username, 'password': password}

    client = Client(enforce_csrf_checks=True)

    resp = client.post(url, data=data)
    assert resp.status_code == 403

    client = Client()
    resp = client.post(url, data=data)
    assert resp.status_code == 302

