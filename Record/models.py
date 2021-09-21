from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import date, datetime

class Product(models.Model):
    
    Categories =(
        ("banku", "banku"),
        ("kenkey", "kenkey"),
        ("rice", "rice"),
        ("fufu", "fufu"),
        ("burger", "burger"),
        ("pizza", "pizza")
        )
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='product', default="1")
    owner = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=50)
    Published = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices = Categories)
    available = models.BooleanField(default= False)

            
    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-Published",)


class Profile(models.Model):
    prouser = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/")
    bio = models.TextField(blank=True,default ="null")
    interest = models.TextField(blank=True,default ="null")
    created = models.DateTimeField(auto_now=False, auto_now_add=True,blank=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(prouser=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.prouser.username
        

class Employee(models.Model):
    employee_name = models.ForeignKey("auth.User", on_delete=models.CASCADE,default='1')
    owner = models.CharField(max_length=50)
    product = models.CharField(max_length=250)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total_price = models.CharField(max_length=50)
    Published = models.DateField(auto_now=False, auto_now_add=True)

            
    def __str__(self):
        return self.product

    class Meta:
        ordering = ("-Published",)
