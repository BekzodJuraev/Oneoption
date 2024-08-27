from django.db import models
from backend.models import Referral
# Create your models here.
class Userbroker(models.Model):
    email=models.EmailField(unique=True)


    def __str__(self):
        return self.email