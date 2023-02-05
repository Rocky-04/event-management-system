import json
import os

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from events.models import EventType

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_manager.settings")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(username='test_user', password='password')


@pytest.mark.django_db
def test_create_event(api_client, user):
    url = reverse('create')
    api_client.force_authenticate(user=user)
    data = {
        "event_type": "test_event_type",
        "info": json.dumps({"key": "value"}),
        "timestamp": "2023-02-07T00:00:00Z"
    }

    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['user'] == user.pk
    assert response.data['event_type'] == 1
    assert response.data['info'] == '{"key": "value"}'


@pytest.mark.django_db
def test_create_event_with_existing_event_type(api_client, user):
    url = reverse('create')
    EventType.objects.create(name="existing_event_type")
    api_client.force_authenticate(user=user)
    data = {
        "event_type": "existing_event_type",
        "info": json.dumps({"key": "value"}),
        "timestamp": "2023-02-07T00:00:00Z"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['user'] == user.pk
    assert response.data['event_type'] == 1
    assert response.data['info'] == '{"key": "value"}'


@pytest.mark.django_db
def test_create_event_unauthorized(api_client):
    url = reverse('create')
    data = {
        "event_type": "existing_event_type",
        "info": json.dumps({"key": "value"}),
        "timestamp": "2023-02-07T00:00:00Z"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize('data', [
    {"event_type": "", "info": '', "timestamp": "2023-02-07T00:00:00Z"},
    {"event_type": "", "info": json.dumps({"key": "value"}), "timestamp": "2023-02-07T00:00:00Z"},
    {"event_type": "test_event_type", "info": '', "timestamp": "2023-02-07T00:00:00Z"},
    {"event_type": "test_event_type", "info": json.dumps({"key": "value"}), "timestamp": ""},
    {"event_type": "test_event_type", "info": 'text', "timestamp": "2023-02-07T00:00:00Z"},
    {"event_type": "test_event_type", "info": json.dumps({"key": "value"}),
     "timestamp": "invalid_timestamp"},
])
@pytest.mark.django_db
def test_create_event_wrong_data(api_client, user, data):
    url = reverse('create')
    api_client.force_authenticate(user=user)

    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
