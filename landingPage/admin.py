from django.contrib import admin
from .models import Booking,Event,Data_user,Rating
# Register your models here.



admin.site.register(Booking)
admin.site.register(Event)
admin.site.register(Data_user)
admin.site.register(Rating)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)