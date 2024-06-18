from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .serializers import LoginFormSerializer,RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        next_url = request.data.get('next')
        form = LoginFormSerializer(data=request.data)

        if form.is_valid():
            email = form.validated_data.get('email')
            password = form.validated_data.get('password')

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)

                if next_url:
                    return Response({'detail': 'Login successful', 'next': next_url}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)

            else:
                return Response({'detail': 'Логин или пароль неверны'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'detail': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Add any additional logic here, such as sending a welcome email
        return Response({'detail': 'Registration successful'}, status=status.HTTP_201_CREATED)