from django.db import models
from backend.models import Referral
# Create your models here.
class UserProfile(models.Model):
    nickname = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey("User", models.DO_NOTHING)
    ref = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='ref', null=True, blank=True)



    class Meta:
       # managed=False
        db_table = 'user_profile'

class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=150, blank=True, null=True)
    disabled = models.BooleanField()
    verified = models.BooleanField()
    two_level_verified = models.BooleanField()
    uid = models.UUIDField(unique=True)
    ip_address = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'


    def __str__(self):
        return self.email
