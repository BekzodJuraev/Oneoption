from django.contrib import admin
from .models import Profile,PasswordReset,Referral,Click_Referral,FTD,Wallet_Type,Wallet,Withdraw

@admin.register(Withdraw)
class Withdraw(admin.ModelAdmin):
    pass

@admin.register(Wallet_Type)
class Wallet_Type(admin.ModelAdmin):
    pass
@admin.register(Wallet)
class Wallet(admin.ModelAdmin):
    pass

@admin.register(FTD)
class FTDadmin(admin.ModelAdmin):
    list_display = ['user_broker','ftd']
@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    list_display = ['username','email']

# Register your models here.
@admin.register(PasswordReset)
class PasswordReset(admin.ModelAdmin):
    list_display = ['email','token']


@admin.register(Referral)
class Referral(admin.ModelAdmin):
    list_display = ['profile','code','referral_type']

@admin.register(Click_Referral)
class Click_Referral(admin.ModelAdmin):
    list_display = ['referral_link','created_at']