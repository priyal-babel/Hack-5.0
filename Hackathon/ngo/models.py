from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class User(AbstractUser):
    is_ngo = models.BooleanField('ngo status', default=False)
    is_eventManager = models.BooleanField('eventManager status', default=False)
    name = models.CharField(max_length=50,default=' ')
    manager_name = models.CharField(max_length=50,default=' ')
    phone_number = models.CharField(max_length=12,default=' ')
    email = models.EmailField(default='')
    address = models.TextField(default=' ')  
    state = models.CharField(max_length=50,default=' ') 
    city = models.CharField(max_length=50,default=' ')
    zipcode = models.CharField(max_length=10)

class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True) 

    def __str__(self):
        return self.user.username

class EventManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    
    def __str__(self):
        return self.name