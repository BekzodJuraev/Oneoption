from django.contrib.auth.models import User
from .models import Profile,Referral,FTD
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver




@receiver(post_save,sender=Profile)
def create_profile_for_user(sender,instance,created,*args,**kwargs):
    if created:
        Referral.objects.create(profile=instance, referral_type='doxod')
        Referral.objects.create(profile=instance, referral_type='oborot')
        Referral.objects.create(profile=instance, referral_type='sub')
    if instance.recommended_by and hasattr(instance.recommended_by, 'profile') and instance.deposit > 0:
        try:
            FTD.objects.get(profile=instance)
        except FTD.DoesNotExist:
            FTD.objects.create(
                profile=instance,
                recommended_by=instance.recommended_by.profile,
                ftd=instance.deposit
            )
