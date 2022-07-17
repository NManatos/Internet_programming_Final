from django.contrib import admin
from django.urls import path
from landingPage import views
from .models import Event,Booking,User
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name="index"),
    path('register/',views.register,name="register"),
    path('login/', views.loginForm, name="login"),
    path('booking/',views.booking,name="booking"),
    path('logout/',views.logout_user,name="logout")
]
