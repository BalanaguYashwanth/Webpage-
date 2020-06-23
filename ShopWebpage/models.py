from django.db import models


# Create your models here.
class details(models.Model):
    person=models.CharField(max_length=150)
    place=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=150)
   

class orderdetails(models.Model):
    name=models.CharField(max_length=150)
    item=models.TextField()
    time=models.TextField()

    