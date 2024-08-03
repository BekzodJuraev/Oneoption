from django.contrib import admin
from .models import User,UserProfile


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['nickname']


@admin.register(User)
class UserProfile(admin.ModelAdmin):
    pass
# Register your models here.
