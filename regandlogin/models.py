from django.db import models
   

# Create your models here.

class Reg(models.Model):
    firstName=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email=models.EmailField()
    username=models.CharField(max_length=10,primary_key=True)
    password=models.IntegerField()
    confpassword=models.IntegerField()
