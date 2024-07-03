from django.db import models
from django.contrib.auth.models import User
import uuid

class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=140)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()



    def save(self, *args, **kwargs):
        # Update the associated User's email before saving
        if self.username.email != self.email:
            self.username.email = self.email
            self.username.save(update_fields=['email'])


        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Referral(models.Model):
    REFERRAL_TYPES = (
        ('doxod', 'Doxod'),
        ('oborot', 'Oborot'),
        ('sub', 'Sub'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    referral_type = models.CharField(max_length=20, choices=REFERRAL_TYPES)

    def __str__(self):
        return f"{self.profile.email}"