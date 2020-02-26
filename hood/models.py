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
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name="hood")


    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to="images",default="profile.png")
    location = models.CharField(max_length=50)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.SET_NULL,null=True,blank=True,related_name="hoodmember")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def __str__(self):
        return f"{self.user.username} profile"

class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=90)
    desciption = models.TextField(blank=True)
    neighbourhood  = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name="business")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner")

    def create_business(self):
        return self.save()


    def delete_business(self):
        return self.delete()

    def __str__(self):
        return f"{self.name} Business"

class Post(models.Model):
    post = models.CharField(max_length=1000,null=True)
    date= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="postowner")
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name="posthood")