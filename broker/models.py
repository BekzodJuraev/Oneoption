from django.db import models
from backend.models import Referral
import uuid
# Create your models here.
class Userbroker(models.Model):
    email=models.EmailField(unique=True)
    ref_broker = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='ref_broker',
                                       null=True, blank=True)


    def __str__(self):
        return self.email