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

class CartDb(models.Model):
    username=models.CharField(max_length=40,blank=True,null=True)
    product_name=models.CharField(max_length=50,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)

class CheckoutDb(models.Model):
    fullname=models.CharField(max_length=40,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    place=models.CharField(max_length=40,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    total_amount=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=40,blank=True,null=True)
    message=models.TextField(blank=True,null=True)
