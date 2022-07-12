from http.client import HTTPResponse
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponse
from datetime import date
from .models import Event,Booking,User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def index(request):
    return render(request,'landingPage/index.html',
    {   "Events": Event.objects.all(),
        "Bookings": Booking.objects.all(),
        "Users": User.objects.all()
    })


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': ("Please enter a correct %(username)s and password."
                          "Note that both fields may be case-sensitive."),
        'inactive': ("This account is inactive"),
    }

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        #print(form.errors)
        if form.is_valid():
            form.save()
        else:
            form = UserCreationForm()
            
    context = {'form':form} 
    return render(request,'register.html',context)

def login(request):
    if request.method =='POST':
        auth_form=AuthenticationForm(data=request.POST)
        #if auth_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username,password = password)

        if auth:
            if auth.is_active:
                login(request, auth)
                return HttpResponseRedirect('')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        auth_form=AuthenticationForm()
        context = {'form':auth_form} 
        return render(request,'login.html',context)



def book(request, event_id):
    if request.method == "POST":
        try:
            user = User.objects.get(Event.description(request.POST["user"]))
            booking = Booking.objects.get(pk=event_id)
            Event.seats -= 1
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no event chosen")
        except Booking.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: Event does not exist")
        except User.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: User does not exist")
        User.Booking.add(booking)
        return HttpResponseRedirect(reverse("Event", args=(event_id,)))