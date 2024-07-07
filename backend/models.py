from django.db import models
from django.contrib.auth.models import User
import uuid
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True
class PasswordReset(Base):
    email = models.EmailField()
    token = models.CharField(max_length=100)


class Profile(Base):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=140)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    recommended_by = models.ForeignKey('Referral', on_delete=models.CASCADE, related_name='recommended_profiles', null=True, blank=True)

    photo = models.ImageField()



    def save(self, *args, **kwargs):
        # asd
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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='referal')
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    referral_type = models.CharField(max_length=20, choices=REFERRAL_TYPES)

    def __str__(self):
        return f"{self.profile.email}:{self.referral_type} "



