from django.db import models
from datetime import datetime

# Create your models here.
class newsDB(models.Model):
    Fullname=models.CharField(max_length=100)
    Eaddress=models.CharField(max_length=100)

class contactDB(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)

class UserBlogDB(models.Model):
    Category = models.CharField(max_length=100)
    Blog_Title = models.CharField(max_length=500)
    Date = models.DateField(max_length=100)
    Author = models.CharField(max_length=100)
    Blog_Image = models.ImageField(upload_to="Blogs")
    City = models.CharField(max_length=100)
    Content = models.CharField(max_length=10000000)


class UserCategoryDB(models.Model):
    Category = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="Category")
    Description = models.CharField(max_length=1000)

class UserRegDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)

class commentdb(models.Model):
    # Name=models.CharField(max_length=100,null=True,blank=True)
    blog=models.IntegerField(null=True,blank=True)
    Comment=models.CharField(max_length=1000,null=True,blank=True)
    # Email=models.EmailField(max_length=100,null=True,blank=True)
    date = models.DateField(default=datetime.now)

class blogsdb(models.Model):
    Category = models.CharField(max_length=100)
    Blog_Title = models.CharField(max_length=500)
    Date = models.DateField(max_length=100)
    Author = models.CharField(max_length=100)
    Blog_Image = models.ImageField(upload_to="Blogs")
    City = models.CharField(max_length=100)
    Content = models.CharField(max_length=10000000)

class cartdb(models.Model):
    Username=models.CharField(max_length=100)