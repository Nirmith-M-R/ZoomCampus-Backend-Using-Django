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
    rating = models.FloatField(default=0)
    # rides = models.JSONField(default=[])

class ActiveUser(models.Model):
    mail = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    phNo = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    route = models.JSONField()
    rating = models.FloatField(default=0)
    gate = models.IntegerField(default=10)
    
class Rider(models.Model):
    mail = models.CharField(max_length=30, primary_key=True)
    seats = models.IntegerField()
    regNo = models.CharField(max_length=10)

class RiderAccept(models.Model):
    corider_name = models.CharField(max_length=30)
    corider_mail = models.CharField(max_length=30)
    corider_gender = models.CharField(max_length=6)
    corider_phNo = models.CharField(max_length=10)
    corider_gate = models.IntegerField()
    corider_dest = models.CharField(max_length=30)
    rider_mail = models.CharField(max_length=30)

class RideStarted(models.Model):
    rider_mail = models.CharField(max_length=30)
    corider_mail = models.CharField(max_length=30)
    rider_phNo = models.CharField(max_length=30)
    corider_phNo = models.CharField(max_length=30)

