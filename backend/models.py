from django.db import models
from django.contrib.auth.models import User
import uuid
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



        # if self.pk:
        #     current_instance=Profile.objects.get(pk=self.pk)
        #     if current_instance.deposit > self.deposit:
        #         amout=current_instance.deposit - self.deposit
        #
        #         self.withdraw += amout

        #self.total += self.deposit
        self.total_income= self.income_oborot + self.income_doxod



        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


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

