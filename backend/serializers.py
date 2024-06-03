from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User



class LoginFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
