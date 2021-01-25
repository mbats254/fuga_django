from django.db import models
from officers.models import Officer
from django.conf import settings

# Create your models here.
class Farmers(models.Model):
    name = models.CharField(max_length=70)
    county= models.CharField(max_length=64)
    phone_no  = models.CharField(max_length=64, unique=True)    
    uniqid = models.CharField(max_length=12, default='uniqid_unset')  
    def __str__(self):
        return f"{self.name}"


class Breeds(models.Model):
    name = models.CharField(max_length=70)
  
    uniqid = models.CharField(max_length=12, default='uniqid_unset')  
    def __str__(self):
        return f"{self.name}"

class Animals(models.Model):
    name = models.CharField(max_length=70)
    breed = models.ForeignKey(Breeds,on_delete=models.CASCADE,related_name="breed_id", default=0)
    uniqid = models.CharField(max_length=12, default='uniqid_unset')  
    def __str__(self):
        return f"{self.name}"        


class Farm(models.Model):
    farmer_id =  models.ForeignKey(Farmers,on_delete=models.CASCADE,related_name="farmer_id",default=0)  
    uniqid = models.CharField(max_length=12,default='uniqid_unset') 
    def __str__(self):
        return f"{self.id}"
    
class Farmers_Animals(models.Model):
   farm_id  = models.ForeignKey(Farm,on_delete=models.CASCADE,related_name="farm_id",default=0)
   animal_id  = models.ForeignKey(Animals,on_delete=models.CASCADE,related_name="animal_id", default=0)
   uniqid = models.CharField(max_length=12, default='uniqid_unset')  
   def __str__(self):
        return f"{self.name}"   

class Visits(models.Model):
    vet_id = models.ForeignKey(Officer,on_delete=models.CASCADE,related_name="vet_id",default=0) 
    # farm = models.ForeignKey(Farm,on_delete=models.CASCADE,related_name="farm_identity")       
    visit_date = models.DateTimeField()
    uniqid = models.CharField(max_length=12, default='uniqid_unset')  
    def __str__(self):
        return f"{self.visit_date}"        

