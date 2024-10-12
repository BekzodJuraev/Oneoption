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





    def __str__(self):
        return self.email