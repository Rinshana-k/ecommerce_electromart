from django.db import models

# Create your models here.
class UserRegistrationDb(models.Model):
    UserName=models.CharField(max_length=100,blank=True,null=True)
    Password=models.CharField(max_length=100,blank=True,null=True)
    ConfirmPassword=models.CharField(max_length=100,blank=True,null=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)

class ContactDb(models.Model):
    Name=models.CharField(max_length=40,blank=True,null=True)
    Email=models.EmailField(max_length=40,blank=True,null=True)
    Phone=models.IntegerField(blank=True,null=True)
    Subject=models.CharField(max_length=40,blank=True,null=True)
    Message=models.TextField(blank=True,null=True)
