from django.db import models

from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class CategoryDB(models.Model):
     Category=models.CharField(max_length=100,null=True,blank=True)
     Image=models.ImageField(upload_to="Category",null=True,blank=True)
     Description=models.CharField(max_length=1000,null=True,blank=True)

class BlogDB(models.Model):
     Category=models.CharField(max_length=100,null=True,blank=True)
     Blog_Title=models.CharField(max_length=500,null=True,blank=True)
     Date=models.DateField(max_length=100,null=True,blank=True)
     Author=models.CharField(max_length=100,null=True,blank=True)
     Blog_Image=models.ImageField(upload_to="Blogs",null=True,blank=True)
     City=models.CharField(max_length=100,null=True,blank=True)
     Content=models.CharField(max_length=10000000,null=True,blank=True)







