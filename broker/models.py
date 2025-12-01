from django.db import models
from backend.models import Base,Referral
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
# Create your models here.
class Userbroker(Base):
    email=models.EmailField(unique=True)
    broker_ref = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='register_by_ref_user_broker',
                                    null=True, blank=True)
    nickname=models.CharField(max_length=200)
    broker_user_id = models.BigIntegerField(unique=True)
    country_code=models.CharField(max_length=50)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    withdraw = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    doxodnost = models.IntegerField(
        default=1,  # минимальное значение
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    oborot=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profit=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # def save(self, *args, **kwargs):
    #     level_to_doxodnost = {
    #         1: 40,
    #         2: 50,
    #         3: 60,
    #         4: 70,
    #         5: 80,
    #     }
    #
    #     # Get the profile level
    #     level = self.broker_ref.profile.level
    #
    #     # Set doxodnost based on profile level, defaulting to 0 if level is not in the dictionary
    #     self.doxodnost = level_to_doxodnost.get(level, 0)
    #
    #     # Call the superclass save method
    #     super().save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         current_instance = Userbroker.objects.get(pk=self.pk)
    #         if current_instance.deposit > self.deposit:
    #             amout = current_instance.deposit - self.deposit
    #
    #             self.withdraw += amout









    def __str__(self):
        return self.email