from django.contrib import admin
from django.urls import path
from landingPage import views
from .models import Event,Booking,User
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name="index"),
]
