from django.db import models

# Create your models here.
class requests(models.Model):
    name = models.CharField(max_length=30,default="")
    hospital_name = models.CharField(max_length=30,default="")
    blood_group = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    mob_no = models.CharField(max_length=12,default="")

class messages(models.Model):
    name = models.CharField(max_length=30)
    mes = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=30,default="")