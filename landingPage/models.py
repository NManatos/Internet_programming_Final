from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserLabel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField(null=True, blank=True, max_length = 100)


class Event(models.Model):
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=64)
    seats = models.IntegerField(null=True)
    price = models.FloatField(blank=True)
    category = models.CharField(max_length=64)
    coverImg = models.ImageField(upload_to='images', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)


class Booking(models.Model):
    objects = None
    seats = models.IntegerField(null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name="bookingEvent")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="bookingUser")

    class Meta:
        app_label = "landingPage"
