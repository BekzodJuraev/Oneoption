from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import F
from django.core.validators import MinValueValidator, MaxValueValidator

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        abstract=True
class PasswordReset(Base):
    email = models.EmailField()
    token = models.CharField(max_length=100)


class Profile(Base):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    nickname = models.CharField(max_length=150)
    email = models.EmailField()
    withdraw=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    level=models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    total_income=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    income_oborot = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    income_doxod = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField()
    sub_ref = models.UUIDField(default=uuid.uuid4, unique=True)
    next_level=models.IntegerField(default=50)
    recommended_by_partner = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='register_by_ref_partner',
                                   null=True, blank=True)
    # broker_ref = models.ForeignKey(Userbroker, on_delete=models.CASCADE, related_name='register_by_ref_user_broker',
    #                                null=True, blank=True)



    def save(self, *args, **kwargs):
        # asd
        if self.username.email != self.email:
            self.username.email = self.email
            self.username.save(update_fields=['email'])








        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
class Type_promo(Base):
    name=models.CharField(max_length=200)
class Promocode(Base):
    name=models.CharField(max_length=200)
    promo_code=models.CharField(max_length=200,unique=True)
    type_of_promocode=models.ForeignKey(Type_promo,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='promo')
    end_time=models.DateTimeField()
    percentage=models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(70)])
    limit=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

class Referral(Base):
    REFERRAL_TYPES = (
        ('doxod', 'Доля дохода'),
        ('oborot', 'Доля оборота')
    )
    Type_enter=(
        ('main','Главная страница '),
        ('register',' Ссылка на регистрацию'),
        #('android',' Ссылка на Android '),
        ('fast',' Быстрый вход в платформу')
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='referal')
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    type=models.CharField(max_length=20,choices=Type_enter)
    referral_type = models.CharField(max_length=20, choices=REFERRAL_TYPES)



    def __str__(self):
        return f"{self.profile.email}:{self.referral_type} "







# class Notifacation(Base):
#     title=models.CharField(max_length=200)
#     message = models.TextField()

class Click_Referral(Base):
    referral_link=models.ForeignKey(Referral,on_delete=models.CASCADE,related_name='referal_link')

    def __str__(self):
        return self.referral_link.referral_type


class FTD(Base):
    from broker.models import Userbroker
    user_broker = models.ForeignKey(Userbroker, on_delete=models.CASCADE, related_name='FTD')
    recommended_by=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recommended')
    ftd=models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user_broker.email





class Wallet(Base):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='wallet')
    type_wallet=models.ForeignKey("Wallet_Type", on_delete=models.CASCADE)
    wallet_id=models.CharField(max_length=100,unique=True)

    class Meta:
        # Ensuring that a profile can only have one wallet of each type
        constraints = [
            models.UniqueConstraint(fields=['profile', 'type_wallet'], name='unique_profile_type_wallet')
        ]

    def __str__(self):
        return  self.type_wallet.name


class Wallet_Type(Base):
    name=models.CharField(max_length=250)
    def __str__(self):
        return  self.name

class Withdraw(Base):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='withdraw_payment')
    wallet= models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=False)


    def __str__(self):
        return  self.profile.email

    def save(self, *args, **kwargs):
        if self.status:
            if self.profile.total_income >= self.amount:
                self.profile.total_income = F('total_income') - self.amount
                self.profile.save(update_fields=['total_income'])
            else:
                self.status=False
        super().save(*args, **kwargs)





