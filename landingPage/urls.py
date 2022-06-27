from django.contrib import admin
from django.urls import path
from landingPage import views



urlpatterns = [
    path('index/', views.index, name="index"),
]