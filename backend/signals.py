from django.contrib.auth.models import User
from .models import Profile,Referral,FTD,Wallet
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import requests

@receiver(pre_save,sender=Wallet)
def create_walet(sender,instance,*args,**kwargs):
    if instance.type_wallet.name == "Bitcoin":
        wallet_address=instance.wallet_id
        api_url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise ValueError("Invalid Bitcoin wallet address.")
    if instance.type_wallet.name == "Trc20":
        wallet_address=instance.wallet_id
        api_url = f"https://api.trongrid.io/v1/accounts/{wallet_address}"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise ValueError("Invalid Trc20 wallet address.")




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

        ftd=FTD.objects.filter(recommended_by=instance.recommended_by.profile).count()
        profile=instance.recommended_by.profile
        new_level = profile.level

        if ftd > 299:
            new_level = 5
        elif ftd > 199:
            new_level = 4
        elif ftd > 99:
            new_level = 3
        elif ftd > 49:
            new_level = 2


        if new_level != profile.level:
            profile.level = new_level
            profile.save()




