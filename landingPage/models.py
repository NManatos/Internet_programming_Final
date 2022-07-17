from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Event(models.Model):
    description = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    seats = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=64)
    coverImg = models.ImageField(upload_to = 'images',blank = True, null = True)
    date = models.DateTimeField(null= True)
    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="landingPage/media/%s" />' % escape(self.coverImg)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return f"{self.description}: at {self.location} genre: {self.category} price :{self.price} euro  available seats: {self.seats} in {self.date}"

class Data_user(models.Model):
      
    #dateOfBirth = models.DateField()
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING,null= True, related_name="user")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True,related_name="userData")
    def __str__(self):
        return f"{self.user}"
    
class Booking(models.Model):
    #booking_id =models.IntegerField()
    seats = models.IntegerField(null= True)
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING,null= True,related_name="bookingEvent")
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null= True,related_name="bookingUser")
    def __str__(self):
         return f"{self.id} {self.event.description} from {self.user.username}"
    
class Rating(models.Model):

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null= True,related_name="ratingUser")
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING,null= True,related_name="ratingEvent")
    rating_value = models.IntegerField(null = True)
    def __str__(self):
        return f"{self.id} {self.event.description} rating :{self.rating_value}  from {self.user.username}"
    
