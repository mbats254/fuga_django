from django.db import models

# Create your models here.
class Farmers(models.Model):
    name = models.CharField(max_length=70)
    county= models.CharField(max_length=64)
    phone_no  = models.CharField(max_length=64, unique=True)  
    uniqid = models.CharField(max_length=12)   
    uniqid = models.CharField(max_length=12, default='jjjj')  
    def __str__(self):
        return f"{self.name}"