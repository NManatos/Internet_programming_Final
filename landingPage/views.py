from asyncio.windows_events import NULL
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponse
from datetime import date
from .models import Event,Booking,Data_user
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from landingPage.custom_forms import BookingForm,RegistrationForm,AuthenticationForm
from django.contrib import messages


def index(request):
    all_bookings = Booking.objects.all()
    all_events = Event.objects.all()
    if request.user.is_authenticated:
        current_user = request.user 
    else:
        current_user = NULL
    for eventData in all_events:   
        for b in all_bookings:
            if eventData.id == b.event.id :
            #eventData= Event.objects.get(pk=b.event.id)
                print(eventData.description)
                if hasattr(eventData,'avail_seats'):
                    eventData.avail_seats -= b.seats
                
                else:
                    eventData.avail_seats = eventData.seats -b.seats
                print(eventData.avail_seats)
            

    #print(current_user)
    return render(request,'landingPage/index.html',
    {   "Events": all_events,
        "Bookings": all_bookings,
        "current_user":current_user
        
    })



def booking(request):
    #print(request.GET)   
    if request.user.is_authenticated:
        current_user = request.user 
    else:
        current_user = NULL
    eventData = Event.objects.get(pk=request.GET["eventID"])
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        
        # print("BIkame")
        # print(request.POST['seats'])
        Booking.objects.create(event = eventData,user = current_user,seats = request.POST['seats'])
        messages.success(request,"Successful Booking")
    context={
        "Event": eventData ,
        "current_user":current_user,
        "form": form
    }
    return render(request,'booking.html',context)
    
 
def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        
        form = RegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():

            form.save()
            #Data_user.objects.create(first = new_user.first_name, last = new_user.last_name ,email = new_user.email,user = new_user)
            #Data_user.user = form.username
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()

    context = {'form':form} 
        
    return render(request,'register.html',context)

def loginForm(request):
    if request.method =='POST':
        auth_form=AuthenticationForm(data=request.POST)
        #if auth_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username = username,password = password)

        if auth:
            if auth.is_active:
                login(request,auth)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        auth_form=AuthenticationForm()
        context = {'form':auth_form} 
        return render(request,'login.html',context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def book(eventID):
    print(eventID)
    return HttpResponseRedirect('booking',event_id = eventID)