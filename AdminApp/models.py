from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    Category_name=models.CharField(max_length=50,blank=True,null=True)
    Description=models.TextField(max_length=500,blank=True,null=True)
    Category_img=models.FileField(upload_to='category images',blank=True,null=True)

class ProductDb(models.Model):
    CategoryName=models.CharField(max_length=100,blank=True,null=True)
    ProductName=models.CharField(max_length=100,blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Short_Description=models.TextField(blank=True,null=True)
    Detailed_Description=models.TextField(blank=True,null=True)
    Brand=models.CharField(max_length=100,blank=True,null=True)
    Product_Image1=models.ImageField(upload_to="Product Images",blank=True,null=True)
    Product_Image2=models.ImageField(upload_to="Product Images",blank=True,null=True)
    Product_Image3=models.ImageField(upload_to="Product Images",blank=True,null=True)
