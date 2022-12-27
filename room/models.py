from django.db import models
from django.contrib.auth.models import User;
# Create your models here.

class Room (models.Model):
    description = models.CharField(max_length=200)
    reserved = models.BooleanField(default=False)
    user_reservation = models.ForeignKey(User, models.SET_NULL,blank=True,null=True,) 


class Alert (models.Model):
    user_alert = models.ForeignKey(User, models.CASCADE)
    contact_date = models.DateField()
    confirmation_date = models.DateField()