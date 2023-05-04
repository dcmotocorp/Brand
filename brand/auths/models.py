from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('investor', 'Investor'),
        ('startup', 'Startup'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES)
    first_name =  models.CharField(max_length=50, default= "")
    last_name =  models.CharField(max_length=50, default= "")
    email = models.EmailField(unique=True)