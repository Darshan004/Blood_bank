from django.db import models

# Create your models here.
class donors(models.Model):
    name = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=30,default="")
    mob_no = models.CharField(max_length=12,default="")
    age = models.CharField(max_length=5,default="")
    blood_group = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)

