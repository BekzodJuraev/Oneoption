from django.contrib import admin
from .models import Profile,PasswordReset,Referral,Register_link


@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    list_display = ['username','email','balance']

# Register your models here.
@admin.register(PasswordReset)
class PasswordReset(admin.ModelAdmin):
    list_display = ['email','token']


@admin.register(Referral)
class Referral(admin.ModelAdmin):
    list_display = ['profile']

@admin.register(Register_link)
class Register_link(admin.ModelAdmin):
    list_display = ['referral','profile','created_at']