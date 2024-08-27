from django.contrib import admin
from .models import Userbroker


@admin.register(Userbroker)
class Userbrokeradmin(admin.ModelAdmin):
    list_display = ['email']


