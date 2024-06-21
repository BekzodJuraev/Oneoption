from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile_for_user(sender,instance,created,*args,**kwargs):
    if created:
        Profile.objects.create(username=instance,email=instance.email)
