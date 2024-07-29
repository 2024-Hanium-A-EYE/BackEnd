import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from data.models import DataModel

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.mark.django_db
def test_create_and_retrieve_data(api_client, user):
    api_client.login(username='testuser', password='testpassword')

    # Create data
    response = api_client.post('/api/yourmodel/', {'name' : 'Test Name'}, format='json')
    assert response.status_code == 201
    assert reponse.data['name'] == 'Test Name'