import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from PIL import Image
import io

User=get_user_model()

@pytest.fixture
def photo():
    file = io.BytesIO()
    image = Image.new('RGB', (100, 100), color='red')
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file
@pytest.fixture
def api():
    return APIClient()

@pytest.fixture
def test_register(api):

    url = reverse('register')
    data={
    "email":"asda23sasf@gmail.com",
    "password": "12346789@@",
    "password2": "12346789@@"
    }
    response = api.post(url,data,format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.get(email="asda23sasf@gmail.com")

@pytest.fixture
def test_login(test_register,api):

    url = reverse('login')
    data={
    "email":"asda23sasf@gmail.com",
    "password": "12346789@@"
    }
    response = api.post(url,data,format='json')


    assert response.status_code == status.HTTP_200_OK
    assert response.data['token']
    return response.data['token']


@pytest.fixture
def test_update_profile(test_login,api):
    token=test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('profile')
    payload={
        "first_name":"Bekzod",
        "last_name":"Juraev"
    }
    response=api.post(url,payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == 'Profile updated'
    return token



@pytest.fixture
def test_photo(test_update_profile,api,photo):
    token = test_update_profile
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('profile')
    payload={
        "photo":photo
    }
    response=api.patch(url,payload)
    assert response.status_code == status.HTTP_200_OK
    return token

@pytest.mark.django_db
def test_profile(test_photo,api):
    token = test_photo
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url=reverse('profile')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == "asda23sasf@gmail.com"



