from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.db import connection
from django.db import models
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.db.models import Sum,Q,Count,F,Max,Prefetch,Value,IntegerField
from .models import PasswordReset,Profile,Referral,Click_Referral,FTD,Wallet,Wallet_Type
from .serializers import  \
    Refferal_count_all,LoginFormSerializer,RegistrationSerializer,PasswordChangeSerializer,ResetPasswordRequestSerializer,PasswordResetSerializer,GetProfile,UpdateProfile,SetPictures,Refferal_Ser,Refferal_list_Ser,Refferal_count_all_,GetProfile_main,GetProfile_main_chart,GetProfile_main_chart_,GetProfile_balance,GetWalletSer,GetWallet_type
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

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: PasswordChangeSerializer()}
    )



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

    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: LoginFormSerializer()}
    )
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
    authentication_classes = [TokenAuthentication]

    serializer_class = RegistrationSerializer


    def get(self,request):
        code = request.query_params.get('code')
        if code:
            get_link=Referral.objects.get(code=code)
            Click_Referral.objects.create(referral_link=get_link)

            return Response({'detail': 'Click to link created'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)




    def post(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        serializer = self.get_serializer(data=request.data, context={'code': code})
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'detail': 'Registration successful'}, status=status.HTTP_201_CREATED)

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token to logout the user
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class SocialLoginView(APIView):
    def get(self, request):

        return redirect('/auth/login/google-oauth2/')

class SocialLoginComplete(APIView):


    def get(self,request):
        token = request.GET.get('token')

        if token:

            try:
                token = Token.objects.get(key=token)
                response_data = {'detail': 'Login successful via google', 'token': token.key}
                return Response(response_data, status=status.HTTP_200_OK)
            except:
                return Response({'detail': 'Not finded token'}, status=status.HTTP_400_BAD_REQUEST)








class RequestPasswordReset(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = ResetPasswordRequestSerializer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ResetPasswordRequestSerializer()}
    )

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
    authentication_classes = [TokenAuthentication]
    serializer_class = PasswordResetSerializer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: PasswordResetSerializer()}
    )

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
    authentication_classes = [TokenAuthentication]
    serializer_class=GetProfile
    permission_classes = [IsAuthenticated,]


    def get_profile(self):
        return Profile.objects.get(username=self.request.user)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile()}
    )
    def get(self,request):
        ftd_count = FTD.objects.filter(recommended_by=self.get_profile()).count()
        get_profile=Profile.objects.only('first_name','first_name','email','photo','level').annotate(ftd_count=Value(ftd_count)).get(username=request.user)





        serializer = self.serializer_class(get_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: UpdateProfile()}
    )
    def post(self, request):
        profile = self.get_profile()
        serializer = UpdateProfile(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: SetPictures()}
    )
    def patch(self,request):
        profile = self.get_profile()
        serializer = SetPictures(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'photo updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRefraldoxod(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_Ser()}
    )
    def get(self,request):
        queryset = Referral.objects.get(profile=self.request.user.profile,referral_type='doxod')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetRefraloborot(APIView):

    authentication_classes = [TokenAuthentication]
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_Ser()}
    )
    def get(self,request):
        queryset = Referral.objects.get(profile=self.request.user.profile,referral_type='oborot')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)




class GetRefralsub(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_Ser()}
    )

    def get(self, request):
        queryset = Referral.objects.get(profile=self.request.user.profile, referral_type='sub')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
class Refer_list(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = Refferal_list_Ser
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_list_Ser(many=True)}
    )
    def get(self,request):
        queryset = Profile.objects.filter(recommended_by__profile=self.request.user.profile)
        email = request.query_params.get('email')
        id = request.query_params.get('id')
        if email:
            queryset=queryset.filter(email=email)
        if id:
            queryset = queryset.filter(id=id)

        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class Referall_count_daily(APIView):
    serializer_class = Refferal_count_all
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_count_all()}
    )
    def get(self,request):
        queryset=Click_Referral.objects.filter(referral_link__profile=self.request.user.profile,created_at__gte=timezone.now() - timedelta(hours=24)).count()
        serializer = self.serializer_class({"count": queryset})
        return Response(serializer.data, status=status.HTTP_200_OK)


class Referall_count_weekly(APIView):
    serializer_class = Refferal_count_all_
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_count_all_(many=True)}
    )
    def get(self,request):
        queryset=Click_Referral.objects.filter(referral_link__profile=self.request.user.profile,created_at__gte=timezone.now() - timedelta(days=7)).values('created_at__date').annotate(count=Count('id'))
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Referall_count_monthly(APIView):
    serializer_class = Refferal_count_all_
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_count_all_(many=True)}
    )
    def get(self,request):
        queryset=Click_Referral.objects.filter(referral_link__profile=self.request.user.profile,created_at__gte=timezone.now() - timedelta(days=29)).values('created_at__date').annotate(count=Count('id'))
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetMain(APIView):
    serializer_class=GetProfile_main
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_main()}
    )

    def get(self,request):
        profile = request.user.profile
        click_all=Click_Referral.objects.filter(referral_link__profile=profile).count()
        register_count=Profile.objects.filter(recommended_by__profile=profile).count()
        ftd=FTD.objects.filter(recommended_by=profile).aggregate(ftd_sum=Sum('ftd'),count=Count('id'))
        witdraw_ref=Profile.objects.filter(recommended_by__profile=profile).aggregate(witdraw_ref=Sum('withdraw'))['witdraw_ref']
        oborot=Profile.objects.filter(recommended_by__profile=profile).aggregate(oborot=Sum('total'))['oborot']





        queryset={
            "all_click":click_all,
            "register_count":register_count,
            "deposit":profile.deposit,
            'ftd_count':ftd['count'],
            'ftd_sum':ftd['ftd_sum'] or 0,
            'witdraw_ref':witdraw_ref or 0,
            'oborot':oborot or 0
        }
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetMain_chart_daily(APIView):
    serializer_class=GetProfile_main_chart
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_main_chart()}
    )

    def get(self,reqeust):
        profile=reqeust.user.profile
        clicks=Click_Referral.objects.filter(referral_link__profile=profile,created_at__gte=timezone.now() - timedelta(hours=24)).count()
        register_count = Profile.objects.filter(recommended_by__profile=profile,created_at__gte=timezone.now() - timedelta(hours=24)).count()
        ftd_count=FTD.objects.filter(recommended_by=profile,created_at__gte=timezone.now() - timedelta(hours=24)).count()
        queryset = {
            "clicks": clicks,
            "register_count": register_count,
            "ftd_count":ftd_count
        }
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
class GetMain_chart_weekly(APIView):
    serializer_class=GetProfile_main_chart_
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_main_chart_(many=True)}
    )
    def get(self,request):
        profile=request.user.profile
        clicks=Click_Referral.objects.filter(referral_link__profile=profile,created_at__gte=timezone.now() - timedelta(days=7)).values('created_at__date').annotate(click_count=Count('id'))
        registrations  = Profile.objects.filter(recommended_by__profile=profile,created_at__gte=timezone.now() - timedelta(days=7)).values('created_at__date').annotate(register_count=Count('id'))
        ftd_count = FTD.objects.filter(recommended_by=profile,created_at__gte=timezone.now() - timedelta(days=7)).values('created_at__date').annotate(ftd_count=Count('id'))
        data = {}
        for click in clicks:
            date = click['created_at__date']
            data[date] = {'clicks': click['click_count'], 'registrations': 0,'ftd_count':0}

        for registration in registrations:
            date = registration['created_at__date']
            if date in data:
                data[date]['registrations'] = registration['register_count']
            else:
                data[date] = {'clicks': 0, 'registrations': registration['register_count'],'ftd_count':0}

        for ftd in ftd_count:
            date = ftd['created_at__date']
            if date in data:
                data[date]['ftd_count'] = ftd['ftd_count']
            else:
                data[date] = {'clicks': 0, 'registrations': 0, 'ftd_count': ftd['ftd_count']}


        queryset = [
            {
                'created_at__date': date,
                'clicks': values['clicks'],
                'register_count': values['registrations'],
                'ftd_count':values['ftd_count']
            }
            for date, values in data.items()
        ]
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class GetMain_chart_monthly(APIView):
    serializer_class = GetProfile_main_chart_
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_main_chart_(many=True)}
    )

    def get(self, request):
        profile = request.user.profile
        clicks = Click_Referral.objects.filter(referral_link__profile=profile,
                                               created_at__gte=timezone.now() - timedelta(days=29)).values(
            'created_at__date').annotate(click_count=Count('id'))
        registrations = Profile.objects.filter(recommended_by__profile=profile,
                                               created_at__gte=timezone.now() - timedelta(days=29)).values(
            'created_at__date').annotate(register_count=Count('id'))
        ftd_count = FTD.objects.filter(recommended_by=profile,
                                       created_at__gte=timezone.now() - timedelta(days=29)).values(
            'created_at__date').annotate(ftd_count=Count('id'))
        data = {}
        for click in clicks:
            date = click['created_at__date']
            data[date] = {'clicks': click['click_count'], 'registrations': 0, 'ftd_count': 0}

        for registration in registrations:
            date = registration['created_at__date']
            if date in data:
                data[date]['registrations'] = registration['register_count']
            else:
                data[date] = {'clicks': 0, 'registrations': registration['register_count'], 'ftd_count': 0}

        for ftd in ftd_count:
            date = ftd['created_at__date']
            if date in data:
                data[date]['ftd_count'] = ftd['ftd_count']
            else:
                data[date] = {'clicks': 0, 'registrations': 0, 'ftd_count': ftd['ftd_count']}



        # Convert to list of dictionaries for serialization
        queryset = [
            {
                'created_at__date': date,
                'clicks': values['clicks'],
                'register_count': values['registrations'],
                'ftd_count': values['ftd_count']
            }
            for date, values in data.items()
        ]
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Profile_balance(APIView):
    serializer_class = GetProfile_balance
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_balance()}
    )
    def get(self,request):
        profile=Profile.objects.filter(username=request.user).values('total_income','income_oborot','income_doxod').first()

        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetWallet(APIView):
    serializer_class = GetWalletSer
    permission_classes = [IsAuthenticated]

    def get(self,request):
        query=Wallet.objects.filter(profile=request.user.profile)
        serializer = self.serializer_class(query,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class GetWalletType(APIView):
    serializer_class=GetWallet_type
    permission_classes = [IsAuthenticated]

    def get(self,request):
        query = Wallet_Type.objects.all()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        pass




def index(request):
    #user=UserProfile.objects.all()
    return render(request,'google.html')
