from django.db import models
from django.utils.timezone import now

# Create your models here.

class SignUP(models.Model):
    mail = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    phNo = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    program = models.CharField(max_length=20)
    route = models.JSONField()

class ActiveUser(models.Model):
    mail = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    phNo = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    program = models.CharField(max_length=20)
    route = models.JSONField()
    
class Rider(models.Model):
    mail = models.CharField(max_length=30, primary_key=True)
    seats = models.IntegerField()
    regNo = models.CharField(max_length=10)

