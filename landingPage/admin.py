from django.contrib import admin
from .models import Booking,Event,User
# Register your models here.



admin.site.register(Booking)
admin.site.register(Event)
admin.site.register(User)