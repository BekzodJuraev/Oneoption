from django.contrib.auth.models import User
from .models import Profile,Referral,FTD
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver




@receiver(post_save,sender=Profile)
def create_profile_for_user(sender,instance,created,*args,**kwargs):
    if created:
        Referral.objects.get_or_create(profile=instance, referral_type='doxod')
        Referral.objects.get_or_create(profile=instance, referral_type='oborot')
        Referral.objects.get_or_create(profile=instance, referral_type='sub')
    if instance.recommended_by and hasattr(instance.recommended_by, 'profile') and instance.deposit > 0:
        FTD.objects.get_or_create(
            profile=instance,
            defaults={
                'recommended_by': instance.recommended_by.profile,
                'ftd': instance.deposit
            }
        )