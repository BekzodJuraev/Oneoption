from django.contrib.auth.models import User
from .models import Profile,Referral,FTD,Wallet
from broker.models import Userbroker
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import requests

@receiver(pre_save,sender=Wallet)
def create_walet(sender,instance,*args,**kwargs):
    if instance.type_wallet.name == "Bitcoin":
        wallet_address = instance.wallet_id
        api_url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise ValueError("Invalid Bitcoin wallet address.")

    elif instance.type_wallet.name == "Trc20":
        wallet_address = instance.wallet_id
        api_url = f"https://api.trongrid.io/v1/accounts/{wallet_address}"
        response = requests.get(api_url)
        if response.status_code != 200:
            raise ValueError("Invalid Trc20 wallet address.")

    elif instance.type_wallet.name == "ERC20":
        wallet_address = instance.wallet_id
        api_url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey=YOUR_ETHERSCAN_API_KEY"
        response = requests.get(api_url)
        if response.status_code != 200 or response.json().get('status') != '1':
            raise ValueError("Invalid ERC20 wallet address.")






@receiver(post_save,sender=Userbroker)
def create_ftd(sender,instance,created,*args,**kwargs):
    if instance.broker_ref and hasattr(instance.broker_ref, 'profile') and instance.deposit >0:
        FTD.objects.get_or_create(
                user_broker=instance,
                defaults={
                    'recommended_by': instance.broker_ref.profile,
                    'ftd': instance.deposit
                }
            )






@receiver(post_save,sender=Profile)
def create_profile_for_user(sender,instance,created,*args,**kwargs):
    if created:
        Referral.objects.get_or_create(profile=instance, referral_type='doxod',type='main')
        Referral.objects.get_or_create(profile=instance, referral_type='doxod', type='register')
        Referral.objects.get_or_create(profile=instance, referral_type='doxod', type='fast')
        #Referral.objects.get_or_create(profile=instance, referral_type='doxod', type='android')
        Referral.objects.get_or_create(profile=instance, referral_type='oborot', type='main')
        Referral.objects.get_or_create(profile=instance, referral_type='oborot', type='register')
        Referral.objects.get_or_create(profile=instance, referral_type='oborot', type='fast')
        #Referral.objects.get_or_create(profile=instance, referral_type='oborot', type='android')






