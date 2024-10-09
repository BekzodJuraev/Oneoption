from django.db import models
from backend.models import Base
import uuid
# Create your models here.
class Userbroker(Base):
    email=models.EmailField(unique=True)
    uuid=models.UUIDField(unique=True)



    def __str__(self):
        return self.email