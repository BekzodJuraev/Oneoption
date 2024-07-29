from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Profile,Referral

class GetProfile_balance(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['total_income', 'income_oborot', 'income_doxod']

class GetProfile_main_chart_(serializers.Serializer):
    clicks=serializers.IntegerField()
    register_count=serializers.IntegerField()
    ftd_count = serializers.IntegerField()
    day=serializers.DateField(source='created_at__date')
class GetProfile_main_chart(serializers.Serializer):
    clicks=serializers.IntegerField()
    register_count=serializers.IntegerField()
    ftd_count=serializers.IntegerField()
class GetProfile_main(serializers.ModelSerializer):
    all_click=serializers.IntegerField()
    register_count=serializers.IntegerField()
    ftd_count=serializers.IntegerField()
    ftd_sum=serializers.DecimalField(max_digits=10, decimal_places=2)
    witdraw_ref=serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model=Profile
        fields=['all_click','register_count','deposit','ftd_count','ftd_sum','witdraw_ref']
class Refferal_count_all_(serializers.Serializer):
    count=serializers.IntegerField()
    day=serializers.DateField(source='created_at__date')
class Refferal_count_all(serializers.Serializer):
    count=serializers.IntegerField()

class Refferal_list_Ser(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','nickname','deposit']
class Refferal_Ser(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields=['code']



class GetProfile(serializers.ModelSerializer):
    ftd_count=serializers.IntegerField()

    class Meta:
        model=Profile
        fields = ['first_name','last_name','email','photo','level','ftd_count']

class UpdateProfile(serializers.ModelSerializer):
    email=serializers.EmailField(required=False)
    class Meta:
        model=Profile
        fields = ['first_name','last_name','email']

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



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
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
        fields = ['email', 'password','password2']



    def create(self, validated_data):
        code=self.context.get('code')

        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        if code:
            try:
                ref = Referral.objects.get(code=code)
                Profile.objects.create(username=user, email=user.email, recommended_by=ref)
            except Referral.DoesNotExist:
                Profile.objects.create(username=user, email=user.email)
        else:
            Profile.objects.create(username=user, email=user.email)



        return user


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data



