from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    list_display = ['username','email','balance']

# Register your models here.
