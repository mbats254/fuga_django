from django.db import models
from uuid import UUID
from django.contrib.auth.models import User
# Create your models here.
class Officer(models.Model):
    name = models.CharField(max_length=70)
    county= models.CharField(max_length=64)
    phone_no  = models.CharField(max_length=64, unique=True)
    id_no = models.CharField(max_length=64, unique=True)
    uniqid = models.CharField(max_length=12)
    email = models.CharField(max_length=50, unique=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} ({self.county})"
