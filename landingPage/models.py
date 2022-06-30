import email
from django.db import models

# Create your models here.

class Booking(models.Model):
    event_id = models.IntegerField(max_length=3)
    event = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} ({self.event})"

class Event(models.Model):
    description = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="eventName")
    location = models.CharField(max_length=64)
    seats = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.description}: at {self.location} genre: {self.category} price :{self.price} euro  available seats: {self.seats}"

class User(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField()
    dateOfBirth = models.DateField()
    event = models.ManyToManyField(Event, blank=True, related_name="users")

    def __str__(self):
        return f"{self.first} {self.last} email : {self.email} Date of Birth : {self.dateOfBirth}"