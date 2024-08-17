from django.contrib.auth.models import User
from social_core.backends.google import GoogleOAuth2
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from .models import Profile
from django.urls import reverse
from django.utils.http import urlencode
class CustomGoogleOAuth2(GoogleOAuth2):
    def complete(self, *args, **kwargs):

        response = super().complete(*args, **kwargs)
        token, created = Token.objects.get_or_create(user=response)
        Profile.objects.get_or_create(username=response, email=response.email)

        params = {
            'token': token.key
        }

        # Reverse the URL for the view
        url = f"http://localhost:5173/google/complete/"

        # Add the query parameters to the URL
        url_with_params = f'{url}?{urlencode(params)}'
        return redirect(url_with_params)
class EmailAuthBackend:

    def authenticate(self,request,username=None,password=None):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist,User.MultipleObjectsReturned):
            return None



    def get_user(self,user_id):
            try:
                return User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return None