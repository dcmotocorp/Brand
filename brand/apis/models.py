from django.db import models

from auths.models import User
# Create your models here.


class Startups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="image/",default=None,blank=True)
    Backgroundimage = models.ImageField(upload_to="image/",default=None,blank=True)
    Status = models.CharField(max_length=400,default=None,blank=True)
    Name = models.CharField(max_length=400,default=None,blank=True)
    location = models.CharField(max_length=400,default=None,blank=True)
    Company_Type = models.CharField(max_length=400,default=None,blank=True)
    Company_rank = models.CharField(max_length=400,default=None,blank=True)
    Website = models.CharField(max_length=400,default=None,blank=True)
    about = models.TextField(default=None,blank=True)
    

