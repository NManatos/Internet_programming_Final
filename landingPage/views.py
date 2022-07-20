from asyncio.windows_events import NULL
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import urls
from django.contrib.auth import signals
from .models import user
from .models import Event,Booking,User
from django.contrib.auth import login, authenticate,logout
#from django.contrib.auth.forms import UserChangeForm
from landingPage.custom_forms import BookingForm,RegistrationForm,AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from rest_framework_json_api import parsers
from landingPage.serializers import EventSerializer
from django.views.generic import TemplateView
#import json
# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#from permission_classes import DjangoModelPermissionsOrAnonReadOnly

def index2(request):
    all_bookings = Booking.objects.all()
    all_events = Event.objects.all()
    all_categories = []
    if request.user.is_authenticated:
        current_user = request.user 
    else:
        current_user = NULL
    
    for eventData in all_events:   
        for b in all_bookings:
            if eventData.id == b.event.id :
                if hasattr(eventData,'avail_seats'):
                    eventData.avail_seats -= b.seats
                
                else:
                    eventData.avail_seats = eventData.seats -b.seats
        if not hasattr(eventData,"avail_seats"):
            eventData.avail_seats = eventData.seats
        if(eventData.category not in all_categories):
            all_categories.append(eventData.category)    
        

    return render(request,'landingPage/index.html',
    {   "Events": all_events,
        "Bookings": all_bookings,
        "current_user":current_user,
        "categories": all_categories
    })



def booking(request): 
    if request.user.is_authenticated:
        current_user = request.user 
    else:
        current_user = NULL
    eventData = Event.objects.get(pk=request.GET["eventID"])
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
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


def profile(request):
    if request.user.is_authenticated:
        current_user = request.user 
    else:
        current_user = NULL
    all_bookings = Booking.objects.all()
    booked_events = []
    booked_seats= {}
    for bookingData in all_bookings :
        if bookingData.user.id == current_user.id :
            if hasattr(booked_seats,str(bookingData.event.id)):
                booked_seats[str(bookingData.event.id)] += bookingData.seats
            else:
                booked_seats[str(bookingData.event.id)] = bookingData.seats
            if bookingData.event not in booked_events :
                booked_events.append(bookingData.event)
    context = {
        #'form':form,
        'booked_events':booked_events,
        'current_user':current_user,
        'booked_seats':booked_seats,     
    }
    return render(request,'profile.html',context)

# class Event_Creator(APIView):
#     parser_classes = (parsers.JSONParser,)

#     def get(self,request):
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         description = request.data['_embedded.events.name']
#         location = request.data['_embedded.venues[0]name']
#         seats = request.data['_embedded.classifications.upcomingEvents._total']
#         price = request.data['_embedded.classifications.upcomingEvents.tmr']
#         category = request.data['_embedded.classifications[0]genre.name']
#         coverImg = request.data['_embedded.images[0]url']
#         date = request.data['_embedded.sales.public.startDateTime']
#         serializer = EventSerializer(description,location,seats,price,category,coverImg,date)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def create_api(self,request):
    
#         response_api= requests.get("https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=324&apikey=pVsFNqZI7GxDGSPZUxoajGxMDiHMotYg")
        
#         data = parser_classes(response_api)

#         serializer = EventSerializer(data=data)
#         serializer.update
#         print(serializer)
#         if(serializer.is_valid()):
#             return
#         else : return Response('Could not save data')





# def event_list(request):
    
#     print("Entered")
#     if request.method == 'GET':
#         #my_django_view(request)
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         #my_django_view(request)
#         data = JSONParser().parse(request)
#         serializer = EventSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)





            
