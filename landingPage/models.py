from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
#user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
class UserLabel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True)
    birthdate = models.DateTimeField(null= True,blank = True)

class Event(models.Model):
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=64)
    seats = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=64)
    coverImg = models.ImageField(upload_to = 'images',blank = True, null = True)
    date = models.DateTimeField(null= True)
    def __str__(self):
         return f"{self.description} {self.location} price: {self.price} date and time : {self.date}"
 

class Booking(models.Model):
    seats = models.IntegerField(null= True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null= True,related_name="bookingEvent")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True,related_name="bookingUser")
    def __str__(self):
         return f"{self.id} {self.event.description} from {self.user.username}"
    class Meta:
        app_label = "landingPage"


