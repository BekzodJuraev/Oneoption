import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from PIL import Image
import io
from backend.models import Profile,Click_Referral,Wallet_Type,Wallet

from django.utils import timezone
from datetime import timedelta
from freezegun import freeze_time

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
    response = api.post(url,data)

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
        "nickname":"Bekawhy",
    }
    response=api.post(url,payload)
    print(response.data)
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
def test_get_doxod(test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('doxod')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_oborot(test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('oborot')
    response = api.get(url)
    print(response.data)

    assert response.status_code == status.HTTP_200_OK

@pytest.fixture
def test_get_sub(test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('sub')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    return response.data['code']


@pytest.fixture
def test_register_refer(test_get_sub,api):
    code = test_get_sub
    url = f'/register/?code={code}'
    data = {
        "email": "pow@gmail.com",
        "password": "12346789@@",
        "password2": "12346789@@"
    }
    response = api.post(url,data)
    data1 = {
        "email": "powerzver98@gmail.com",
        "password": "12346789@@",
        "password2": "12346789@@"
    }
    response1 = api.post(url,data1)
    assert response.status_code == status.HTTP_201_CREATED
    profile=Profile.objects.get(email="pow@gmail.com")
    profile.deposit=100
    profile.save()
    profile.deposit -=50
    profile.withdraw += 50
    profile.save()
    profile2 = Profile.objects.get(email="powerzver98@gmail.com")
    profile2.deposit = 100
    profile2.save()

    assert profile.recommended_by

@pytest.mark.django_db
def test_list_get(test_register_refer,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('list')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_list_get_email(test_login,api):
    token = test_login
    email="powerzver98@gmail.com"
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = f'/referal/list?email={email}'
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_list_get_id(test_register_refer,test_login,api):
    token = test_login
    id = 2
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = f'/referal/list?id={id}'
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


@pytest.fixture
def test_count_link(test_get_sub,api):
    code = test_get_sub
    url = f'/register/?code={code}'
    response = api.get(url)
    response = api.get(url)

    with freeze_time(timezone.now() - timedelta(hours=2)):
        response = api.get(url)
        response = api.get(url)



    with freeze_time(timezone.now() - timedelta(days=6)):
        response = api.get(url)
        response = api.get(url)

    with freeze_time(timezone.now() - timedelta(days=28)):
        response = api.get(url)
        response = api.get(url)

    assert response.status_code == status.HTTP_201_CREATED
    assert Click_Referral.objects.filter(referral_link__code=code).count() == 8








@pytest.mark.django_db
def test_google(api):
    url=reverse('google')
    response=api.get(url)
    assert response.url == "/auth/login/google-oauth2/"



@pytest.mark.django_db
def test_ref_daily_count(test_count_link,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('ref_daily')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_ref_weekly_count(test_count_link,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('ref_weekly')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_ref_mothly_count(test_count_link,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('ref_monthly')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_getprofile_main(test_count_link,test_register_refer,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('profile_main')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_main_chart_daily(test_count_link,test_register_refer,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('main_chart_daily')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
@pytest.mark.django_db
def test_main_chart_weekly(test_count_link,test_register_refer,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('main_chart_weekly')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_main_chart_monthly(test_count_link,test_register_refer,test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('main_chart_monthly')
    response= api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_profile_balance(test_login,api):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url =reverse('profile_balance')
    response= api.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_profile(test_count_link,test_register_refer,test_photo,api):
    token = test_photo
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url=reverse('profile')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == "asda23sasf@gmail.com"

@pytest.fixture
def create_typewallet():
    a, _ = Wallet_Type.objects.get_or_create(name="Bitcoin")
    b, _ = Wallet_Type.objects.get_or_create(name="USDT2")

    # profile = Profile.objects.get(email='asda23sasf@gmail.com')
    #
    # wallet1 = Wallet.objects.create(profile=profile, type_wallet=a, wallet_id="123")
    # wallet2 = Wallet.objects.create(profile=profile, type_wallet=b, wallet_id="1234")

    return a, b


@pytest.mark.django_db
def test_wallet_get(api,test_login,create_typewallet):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('wallet')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK

@pytest.fixture
def test_wallet_post(api,test_login,create_typewallet):
    token = test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('wallet')
    payload={
        'type_wallet':'Bitcoin',
        'wallet_id':'123456'
    }
    response = api.post(url,payload)
    payload1 = {
        'type_wallet': 'Trc20',
        'wallet_id': '123456'
    }
    response1 = api.post(url, payload1)
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_wallet_list(api,test_login,test_wallet_post):
    token=test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('wallet_list')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK



@pytest.mark.django_db
def test_withdraw_get(api,test_login,test_wallet_post):
    token=test_login
    api.credentials(HTTP_AUTHORIZATION='Token ' + token)
    url = reverse('withdraw')
    response = api.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK


