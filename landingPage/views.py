from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import date
from .models import Event,Booking,User
# Create your views here.



def index(request):
    name = "Nick"
    d = date.today()
    return render(request,'landingPage/index.html',
    {   "Events": Event.objects.all()

    })