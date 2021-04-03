from django.db import models

# Create your models here.

class Ngo(models.Model):
    ngo_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)  


    def __str__(self):
        return self.ngo_name

