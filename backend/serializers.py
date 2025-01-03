from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Profile,Referral,Wallet,Wallet_Type

from broker.models import Userbroker

class WithdrawSerPOST(serializers.Serializer):
    wallet=serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)






class WithdrawSer(serializers.Serializer):
    wallet=serializers.CharField(source='type_wallet__name')



class WalletPOST(serializers.ModelSerializer):
    type_wallet = serializers.SlugRelatedField(
        queryset=Wallet_Type.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Wallet
        fields = ['type_wallet', 'wallet_id']


    def create(self, validated_data):
        profile = validated_data.pop('profile')
        wallet = Wallet.objects.create(profile=profile, **validated_data)
        return wallet


class GetWallet_type(serializers.ModelSerializer):
    class Meta:
        model=Wallet_Type
        fields=['name']




class GetProfile_balance(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['total_income', 'income_oborot', 'income_doxod']

class GetProfile_main_chart_(serializers.Serializer):
    clicks=serializers.IntegerField()
    register_count=serializers.IntegerField()
    ftd_count = serializers.IntegerField()
    date=serializers.DateField(source='created_at__date')
class GetProfile_main_chart(serializers.Serializer):
    clicks=serializers.IntegerField()
    register_count=serializers.IntegerField()
    ftd_count=serializers.IntegerField()
    date=serializers.DateTimeField()
class GetProfile_main(serializers.ModelSerializer):
    all_click=serializers.IntegerField()
    register_count=serializers.IntegerField()
    ftd_count=serializers.IntegerField()
    ftd_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    witdraw_ref=serializers.DecimalField(max_digits=10, decimal_places=2)
    oborot=serializers.DecimalField(max_digits=10, decimal_places=2)
    pl = serializers.DecimalField(max_digits=10, decimal_places=2)
    deposit=serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model=Profile
        fields=['all_click','register_count','deposit','ftd_count','ftd_sum','witdraw_ref','pl','oborot']
class Refferal_count_all_(serializers.Serializer):
    count=serializers.IntegerField()
    date=serializers.DateField()

class Refferal_count_all(serializers.Serializer):
    count=serializers.IntegerField()
    date=serializers.DateTimeField()

class PartnerLevelSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    income_percent = serializers.CharField(max_length=10)
    turnover = serializers.CharField(max_length=10)
    deposit = serializers.CharField(max_length=20)

class Refferal_list_Ser(serializers.ModelSerializer):
    flag_photo=serializers.ImageField(default="")
    nickname=serializers.CharField(default="")
    doxod_procent=serializers.IntegerField(default=0,min_value=0,max_value=100)
    oborot=serializers.DecimalField(default=0,max_digits=10, decimal_places=2)
    balance=serializers.DecimalField(default=0,max_digits=10, decimal_places=2)
    profit=serializers.DecimalField(default=0,max_digits=10, decimal_places=2)


    class Meta:
        model=Userbroker
        fields=['id','email','deposit','withdraw','oborot','balance','profit','doxod_procent','nickname','flag_photo']


class Refferal_Ser(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    referral_type = serializers.CharField(source='get_referral_type_display', read_only=True)

    class Meta:
        model=Referral
        fields=['code','type_display','referral_type',]




class GetProfile(serializers.ModelSerializer):
    ftd_count=serializers.IntegerField()

    class Meta:
        model=Profile
        fields = ['nickname','email','photo','level','ftd_count','sub_ref','next_level']

class UpdateProfile(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields = ['nickname','email']

class SetPictures(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['photo']

class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError("New passwords do not match.")
        return data
class LoginFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class ClickToken(serializers.Serializer):
    token_ref = serializers.CharField(required=True)




class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    token_ref=serializers.UUIDField(required=False)
    email=serializers.EmailField(required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists() or Userbroker.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already registered. Please use a different one.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    class Meta:
        model = User
        fields = ['email', 'password','password2','token_ref']



    def create(self, validated_data):

        token_ref = validated_data.get('token_ref')

        if token_ref:
            try:
                ref = Profile.objects.get(sub_ref=token_ref)
            except Referral.DoesNotExist:
                raise serializers.ValidationError({"message": "Token does not exist."})
        else:
            ref = None  # No referral if token_ref not provided


        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        nickname = user.email.split("@")[0]

        # Create the user's profile with or without referral
        profile=Profile.objects.create(
            username=user, email=user.email, nickname=nickname,recommended_by_partner=ref)





        return user

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data



