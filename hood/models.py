from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Neighbourhood(models.Model):
    name  = models.CharField(max_length=50)
    location =models.CharField(max_length=500)
    logo = models.ImageField(upload_to="images",default="hood.png")
    description = models.CharField(max_length=5000)
    RedCross_contact =  models.IntegerField(blank=True,null=True)
    


    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def __str__(self):
        return f"{self.name}"

