from django.db import models
from backend.models import Base,Referral
import uuid
# Create your models here.
class Userbroker(Base):
    email=models.EmailField(unique=True)
    uuid=models.UUIDField(unique=True)
    broker_ref = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='register_by_ref_user_broker',
                                    null=True, blank=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    withdraw = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         current_instance = Userbroker.objects.get(pk=self.pk)
    #         if current_instance.deposit > self.deposit:
    #             amout = current_instance.deposit - self.deposit
    #
    #             self.withdraw += amout









    def __str__(self):
        return self.email