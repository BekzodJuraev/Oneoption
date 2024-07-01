import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User=get_user_model()


@pytest.mark.django_db
def test_register():
    client = APIClient()
    url = reverse('register')
    data={
    "email":"asda23sasf@gmail.com",
    "password": "12346789@@",
    "password2": "12346789@@"
    }
    response = client.post(url,data,format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get(email="asda23sasf@gmail.com")

@pytest.mark.django_db
def test_login():
    test_register()
    client = APIClient()
    url = reverse('login')
    data={
    "email":"asda23sasf@gmail.com",
    "password": "12346789@@"
    }
    response = client.post(url,data,format='json')
    print(f"Login response data: {response.data}")
    print(f"Login response status code: {response.status_code}")

    assert response.status_code == status.HTTP_200_OK
    assert response.data['token']
