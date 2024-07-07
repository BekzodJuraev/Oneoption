from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.sites.models import Site

from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
# Create your views here.
from .models import PasswordReset,Profile,Referral
from .serializers import LoginFormSerializer,RegistrationSerializer,PasswordChangeSerializer,ResetPasswordRequestSerializer,PasswordResetSerializer,GetProfile,UpdateProfile,SetPictures,Refferal_Ser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from social_django.utils import psa
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated



class Change_password(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'success': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    def post(self, request, *args, **kwargs):
        next_url = request.data.get('next')
        form = LoginFormSerializer(data=request.data)

        if form.is_valid():
            email = form.validated_data.get('email')
            password = form.validated_data.get('password')

            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)  # Get or create a token for the user

                response_data = {'detail': 'Login successful', 'token': token.key}
                if next_url:
                    response_data['next'] = next_url

                return Response(response_data, status=status.HTTP_200_OK)

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

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token to logout the user
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class SocialLoginView(APIView):
    def get(self, request):
        return redirect('/auth/login/google-oauth2/')



class RequestPasswordReset(APIView):
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({"error": "User with this email not found"}, status=status.HTTP_404_NOT_FOUND)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        reset = PasswordReset(email=email, token=token)
        reset.save()
        #send_email()

        #reset_url = f"{os.environ['PASSWORD_RESET_BASE_URL']}/{token}"
          # For debugging purposes; remove or use a proper logging system in production

        # Sending reset link via email (commented out for clarity)
        # ... (email sending code)

        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)





class PasswordResetConfirm(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)

        reset_obj = PasswordReset.objects.filter(token=token).first()

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=reset_obj.email)
        except User.DoesNotExist:
            return Response({"error": "Invalid token or user does not exist"}, status=status.HTTP_404_NOT_FOUND)

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        reset_obj.delete()

        return Response({"success": "Password has been reset"}, status=status.HTTP_200_OK)


class Profile_View(APIView):
    serializer_class=GetProfile
    permission_classes = [IsAuthenticated,]


    def get_profile(self):
        return Profile.objects.get(username=self.request.user)

    def get(self,request):
        get_profile=self.get_profile()
        serializer = self.serializer_class(get_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        profile = self.get_profile()
        serializer = UpdateProfile(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        profile = self.get_profile()
        serializer = SetPictures(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'photo updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRefraldoxod(APIView):
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]



    def get(self,request):
        queryset = Referral.objects.get(profile=self.request.user.profile,referral_type='doxod')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetRefraloborot(APIView):
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]



    def get(self,request):
        queryset = Referral.objects.get(profile=self.request.user.profile,referral_type='oborot')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)




class GetRefralsub(APIView):
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        queryset = Referral.objects.get(profile=self.request.user.profile, referral_type='sub')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
