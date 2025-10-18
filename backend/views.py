from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.db import connection
from django.db import models

from rest_framework.throttling import UserRateThrottle
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from broker.models import Userbroker
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
from django.db.models.functions import TruncHour
from django.db.models import Sum,Q,Count,F,Max,Prefetch,Value,IntegerField
from .models import PasswordReset,Profile,Referral,Click_Referral,FTD,Wallet,Wallet_Type,Withdraw
from .serializers import  \
    Refferal_count_all,LoginFormSerializer,RegistrationSerializer,PasswordChangeSerializer,ResetPasswordRequestSerializer,PasswordResetSerializer,GetProfile,UpdateProfile,SetPictures,Refferal_Ser,Refferal_list_Ser,Refferal_count_all_,GetProfile_main,GetProfile_main_chart,GetProfile_main_chart_,GetProfile_balance,GetWallet_type,WalletPOST,WithdrawSer,ClickToken,WithdrawSerPOST,PartnerLevelSerializer,RegisterBroker
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
import requests



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
                return Response({'message': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)
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

                response_data = {'message': 'Login successful', 'token': token.key}
                if next_url:
                    response_data['next'] = next_url

                return Response(response_data, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Логин или пароль неверны'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'message': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)


class Token_Click(APIView):
    serializer_class=ClickToken
    throttle_classes = [UserRateThrottle]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ClickToken()}
    )
    def post(self, request):
        form = self.serializer_class(data=request.data)
        if form.is_valid():
            token_ref = form.validated_data.get('token_ref')
            try:
                get_link = Referral.objects.get(code=token_ref)

                # Check if the user/IP is allowed to proceed
                self.check_throttles(request)

                Click_Referral.objects.create(referral_link=get_link)
                return Response({'message': 'Click to link created'}, status=status.HTTP_201_CREATED)
            except Referral.DoesNotExist:
                return Response({'message': 'Token invalid'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)



class RegistrationAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = RegistrationSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the token to logout the user
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

class SocialLoginView(APIView):
    def get(self, request):
        return redirect('/auth/login/google-oauth2/')

class SocialLoginComplete(APIView):


    def get(self,request):

        token = request.GET.get('token')

        if token:
            try:
                token = Token.objects.get(key=token)
                response_data = {'message': 'Login successful via google', 'token': token.key}
                return Response(response_data, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                return Response({'message': 'Token not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Token parameter missing'}, status=status.HTTP_400_BAD_REQUEST)








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
            return Response({"message": "User with this email not found"}, status=status.HTTP_404_NOT_FOUND)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        reset = PasswordReset(email=email, token=token)
        reset.save()
        send=f"https://one-option.onrender.com/auth/password/reset/confirm/{token}/"
        send_mail(
            'Password reset',
            f'Recovery link {send}',
            'bekawhy2705@gmail.com',
            [email],
            fail_silently=False,
        )



        return Response({'message': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)





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

        if reset_obj is None:
            return Response({"message": "Invalid token or reset object not found"}, status=status.HTTP_404_NOT_FOUND)

        try:

            user = User.objects.get(email=reset_obj.email)
        except User.DoesNotExist:
            return Response({"message": "Invalid token or user does not exist"}, status=status.HTTP_404_NOT_FOUND)

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        reset_obj.delete()

        return Response({"message": "Password has been reset"}, status=status.HTTP_200_OK)


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
        ftd_count = FTD.objects.filter(recommended_by=self.get_profile(),created_at__month=date.today().month).count()

        get_profile=Profile.objects.only('nickname','email','photo','level','next_level').annotate(ftd_count=Value(ftd_count)).get(username=request.user)





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
            return Response({'message': request.data or "Not updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: SetPictures()}
    )
    def patch(self,request):
        profile = self.get_profile()
        serializer = SetPictures(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Photo updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class GetRefral_link(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = Refferal_Ser
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_Ser(many=True)}
    )

    def get(self, request):
        query=Referral.objects.filter(profile=self.request.user.profile)

        serializer = self.serializer_class(query,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Refer_list(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = Refferal_list_Ser
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_list_Ser(many=True)}
    )
    def get(self,request):
        queryset = Userbroker.objects.filter(broker_ref__profile=self.request.user.profile)
        email = request.query_params.get('email')
        id = request.query_params.get('id')
        if email:
            queryset = queryset.filter(email__icontains=email)
        if id:
            queryset = queryset.filter(id=id)

        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PartnerLevelView(APIView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: PartnerLevelSerializer(many=True)}
    )

    def get(self, request):
        PARTNER_LEVELS = [
            {
                "level": 1,
                "income_percent": "40%",
                "turnover": "2%",
                "deposit": "0-49",
            },
            {
                "level": 2,
                "income_percent": "50%",
                "turnover": "3%",
                "deposit": "50-99",
            },
            {
                "level": 3,
                "income_percent": "60%",
                "turnover": "4%",
                "deposit": "100-199",
            },
            {
                "level": 4,
                "income_percent": "70%",
                "turnover": "5%",
                "deposit": "200-250",
            },
            {
                "level": 5,
                "income_percent": "80%",
                "turnover": "7%",
                "deposit": "Более 300",
            }
        ]

        serializer = PartnerLevelSerializer(PARTNER_LEVELS, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Referall_count_daily(APIView):
    serializer_class = Refferal_count_all
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_count_all(many=True)}
    )
    def get(self,request):
        start_time = timezone.now() - timedelta(hours=24)



        time_range = [
            start_time + timedelta(hours=x)
            for x in range(0, 25)  # 25 to include the current hour
        ]

        # Initialize a dictionary with default values for each hour
        data = {
            hour.replace(minute=0, second=0, microsecond=0): {'click_count': 0}
            for hour in time_range
        }

        # Query the database for click data
        queryset = Click_Referral.objects.filter(
            referral_link__profile=request.user.profile,
            created_at__gte=start_time
        ).annotate(hour=TruncHour('created_at')).values('hour').annotate(count=Count('id'))


        # Populate the data dictionary with actual click counts
        for click in queryset:
            hour = click['hour']

            data[hour]['click_count'] = click['count']

        # Convert the data to a list for serialization
        response_data = [
            {
                'date': hour,
                'count': values['click_count']
            }
            for hour, values in data.items()
        ]


        serializer = self.serializer_class(response_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Referall_count_weekly(APIView):
    serializer_class = Refferal_count_all_
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_count_all_(many=True)}
    )
    def get(self,request):
        start_date = timezone.now().date() - timedelta(days=7)


        # Prepare a list of all dates for the last 29 days
        date_range = [start_date + timedelta(days=x) for x in range(0, 8)]


        # Initialize a dictionary with default values for each date
        data = {date: {'click_count': 0} for date in date_range}

        # Get click data from the database
        queryset = Click_Referral.objects.filter(
            referral_link__profile=request.user.profile,
            created_at__gte=start_date
        ).values('created_at__date').annotate(count=Count('id'))

        # Populate the data dictionary with actual click counts
        for click in queryset:
            date = click['created_at__date']
            data[date]['click_count'] = click['count']

        # Convert the data to a list for serialization
        response_data = [
            {
                'date': date,
                'count': values['click_count']
            }
            for date, values in data.items()
        ]

        # Serialize the response data
        serializer = self.serializer_class(response_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Referall_count_monthly(APIView):
    serializer_class = Refferal_count_all_
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: Refferal_count_all_(many=True)}
    )
    def get(self,request):
        start_date = timezone.now().date() - timedelta(days=29)

        # Prepare a list of all dates for the last 29 days
        date_range = [start_date + timedelta(days=x) for x in range(0, 30)]

        # Initialize a dictionary with default values for each date
        data = {date: {'click_count': 0} for date in date_range}

        # Get click data from the database
        queryset = Click_Referral.objects.filter(
            referral_link__profile=request.user.profile,
            created_at__gte=start_date
        ).values('created_at__date').annotate(count=Count('id'))

        # Populate the data dictionary with actual click counts
        for click in queryset:
            date = click['created_at__date']
            data[date]['click_count'] = click['count']

        # Convert the data to a list for serialization
        response_data = [
            {
                'date': date,
                'count': values['click_count']
            }
            for date, values in data.items()
        ]

        # Serialize the response data
        serializer = self.serializer_class(response_data, many=True)
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

        oborot=0
        pl=0
        register_count=Userbroker.objects.filter(
            broker_ref__profile=profile).count()
        ftd=FTD.objects.filter(recommended_by=profile,created_at__month=date.today().month).aggregate(ftd_sum=Sum('ftd'),count=Count('id'))

        witdraw_ref=Userbroker.objects.filter(broker_ref__profile=profile).aggregate(witdraw_ref=Sum('withdraw'))['witdraw_ref']
        # #oborot=Userbroker.objects.filter(recommended_by__profile=profile).aggregate(oborot=Sum('total'))['oborot']
        deposit=Userbroker.objects.filter(broker_ref__profile=profile).aggregate(deposit=Sum('deposit'))['deposit']





        queryset={
            "all_click":click_all,
            "register_count":register_count,
            "deposit":deposit or 0,
            'ftd_count':ftd['count'],
            'ftd_sum':ftd['ftd_sum'] or 0,
            'witdraw_ref': witdraw_ref or 0,
            'pl':pl,
            'oborot':oborot or 0
        }
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetMain_chart_daily(APIView):
    serializer_class=GetProfile_main_chart
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_main_chart(many=True)}
    )

    def get(self,request):
        profile = request.user.profile
        start_time = timezone.now() - timedelta(hours=24)

        # Clicks aggregated by hour
        clicks = Click_Referral.objects.filter(
            referral_link__profile=profile,
            created_at__gte=start_time
        ).annotate(hour=TruncHour('created_at')).values('hour').annotate(click_count=Count('id')).order_by('hour')

        # Registrations aggregated by hour
        registrations = Userbroker.objects.filter(
            broker_ref__profile=profile,
            created_at__gte=start_time
        ).annotate(hour=TruncHour('created_at')).values('hour').annotate(register_count=Count('id')).order_by('hour')

        # FTDs aggregated by hour
        ftds = FTD.objects.filter(
            recommended_by=profile,
            created_at__gte=start_time
        ).annotate(hour=TruncHour('created_at')).values('hour').annotate(ftd_count=Count('id')).order_by('hour')

        # Initialize data dictionary for 24 hours
        data = {
            hour.replace(minute=0, second=0, microsecond=0): {
                'clicks': 0, 'registrations': 0, 'ftd_count': 0
            }
            for hour in [start_time + timedelta(hours=i) for i in range(25)]
        }

        # Populate data dictionary with actual counts
        for entry in clicks:
            data[entry['hour']]['clicks'] = entry['click_count']

        for entry in registrations:
            data[entry['hour']]['registrations'] = entry['register_count']

        for entry in ftds:
            data[entry['hour']]['ftd_count'] = entry['ftd_count']

        # Prepare response data
        response_data = [
            {
                'date': hour,
                'clicks': values['clicks'],
                'register_count': values['registrations'],
                'ftd_count': values['ftd_count']
            }
            for hour, values in data.items()
        ]

        # Serialize response data
        serializer = self.serializer_class(response_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class GetMain_chart_weekly(APIView):
    serializer_class=GetProfile_main_chart_
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetProfile_main_chart_(many=True)}
    )
    def get(self,request):
        profile=request.user.profile
        start_date = timezone.now().date() - timedelta(days=7)

        # Prepare a list of all dates within the last 7 days (only dates)
        date_range = [start_date + timedelta(days=x) for x in range(0, 8)]

        # Initialize a dictionary to ensure all dates have default values (using only dates)
        data = {date: {'clicks': 0, 'registrations': 0, 'ftd_count': 0} for date in date_range}

        # Get the click data (convert created_at to date in the query)
        clicks = Click_Referral.objects.filter(
            referral_link__profile=profile,
            created_at__gte=start_date
        ).values('created_at__date').annotate(click_count=Count('id'))

        # Get the registration data (convert created_at to date in the query)
        registrations = Userbroker.objects.filter(
            broker_ref__profile=profile,
            created_at__gte=start_date
        ).values('created_at__date').annotate(register_count=Count('id'))

        # Get the FTD count data (convert created_at to date in the query)
        ftd_count = FTD.objects.filter(
            recommended_by=profile,
            created_at__gte=start_date
        ).values('created_at__date').annotate(ftd_count=Count('id'))

        # Populate the data dictionary with actual click, registration, and FTD data
        for click in clicks:
            date = click['created_at__date']
            data[date]['clicks'] = click['click_count']

        for registration in registrations:
            date = registration['created_at__date']
            data[date]['registrations'] = registration['register_count']

        for ftd in ftd_count:
            date = ftd['created_at__date']
            data[date]['ftd_count'] = ftd['ftd_count']

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

        # Serialize and return the response
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
        start_date = timezone.now() - timedelta(days=29)

        # Prepare a list of all dates within the last 29 days
        date_range = [start_date + timedelta(days=x) for x in range(0, 30)]

        # Initialize a defaultdict to ensure all dates have default values
        data = {date.date(): {'clicks': 0, 'registrations': 0, 'ftd_count': 0} for date in date_range}

        # Get the click data
        clicks = Click_Referral.objects.filter(referral_link__profile=profile,
                                               created_at__gte=start_date).values(
            'created_at__date').annotate(click_count=Count('id'))

        # Get the registration data
        registrations = Userbroker.objects.filter(
            broker_ref__profile=profile,
            created_at__gte=start_date
        ).values('created_at__date').annotate(register_count=Count('id'))

        # Get the FTD count data
        ftd_count = FTD.objects.filter(recommended_by=profile,
                                       created_at__gte=start_date).values(
            'created_at__date').annotate(ftd_count=Count('id'))

        # Populate the data dictionary with actual click, registration, and FTD data
        for click in clicks:
            date = click['created_at__date']
            data[date]['clicks'] = click['click_count']

        for registration in registrations:
            date = registration['created_at__date']
            data[date]['registrations'] = registration['register_count']

        for ftd in ftd_count:
            date = ftd['created_at__date']
            data[date]['ftd_count'] = ftd['ftd_count']

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

        # Serialize and return the response
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
    serializer_class = WalletPOST
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: WalletPOST()}
    )




    def get(self,request):
        query=Wallet.objects.filter(profile=request.user.profile)
        serializer = self.serializer_class(query,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class GetWalletType(APIView):
    serializer_class=GetWallet_type
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: GetWallet_type()}
    )

    def get(self,request):
        query = Wallet_Type.objects.all()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: WalletPOST()}
    )
    def post(self,request):
        try:
            serializer = WalletPOST(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(profile=request.user.profile)
            return Response({'message': 'Added Wallet', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            raise ValidationError({"message": str(e)}, code=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:

            if 'wallet' in str(e):  # Check if the error mentions the 'wallet' field
                raise ValidationError({"message": "A wallet with this type wallet already exists."},
                                      code=status.HTTP_400_BAD_REQUEST)
            else:

                raise ValidationError({"message": "Database integrity error occurred."},
                                      code=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response({'message': 'An error occurred', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Withdraw_View(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=WithdrawSer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: WithdrawSer()}
    )

    def get(self,request):
        query=Wallet.objects.filter(profile=request.user.profile).values('type_wallet__name')
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: WithdrawSerPOST()}
    )

    def post(self,request):
        profile=request.user.profile
        serializer = WithdrawSerPOST(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            wallet = serializer.validated_data['wallet']

            try:
                # Retrieve the wallet for the user's profile
                get_profile = Wallet.objects.get(profile=profile, type_wallet__name=wallet)


                if profile.total_income >= amount:
                    Withdraw.objects.create(profile=profile,wallet=get_profile,amount=amount)

                    # profile.total_income = F('total_income') - amount
                    # profile.save()



                    return Response({'message': 'Withdraw Proccessing', 'data': serializer.data},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Not enough money"}, status=status.HTTP_400_BAD_REQUEST)

            except Wallet.DoesNotExist:
                return Response({"message": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class RegisterBrokerView(APIView):
    serializer_class = RegisterBroker

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: RegisterBroker()}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            email = serializer.validated_data['email']

            try:
                broker = Referral.objects.get(code=token)
            except Referral.DoesNotExist:
                return Response({'error': 'Invalid broker token'}, status=400)

            Userbroker.objects.create(email=email, broker_ref=broker)

            return Response({'message': 'Broker registered successfully'}, status=201)

        return Response(serializer.errors, status=400)



