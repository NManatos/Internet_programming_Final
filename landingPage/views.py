from asyncio.windows_events import NULL
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Event, Booking, UserLabel
from django.contrib.auth import login, authenticate, logout
from .custom_forms import BookingForm, RegistrationForm, AuthenticationForm,UserLabelForm,CustomUserChangeForm,mDateTimeField
from django.contrib import messages
from django.http import HttpResponse
#from django import forms
#from spec_widget import FormField, MetaForm
from django.contrib.auth.forms import UserChangeForm, UsernameField


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
            if eventData.id == b.event.id:
                if hasattr(eventData, 'avail_seats'):
                    eventData.avail_seats -= b.seats

                else:
                    eventData.avail_seats = eventData.seats - b.seats
        if not hasattr(eventData, "avail_seats"):
            eventData.avail_seats = eventData.seats
        if (eventData.category not in all_categories):
            all_categories.append(eventData.category)

    return render(request, 'landingPage/index.html',
                  {"Events": all_events,
                   "Bookings": all_bookings,
                   "current_user": current_user,
                   "categories": all_categories
                   })


def booking(request):
    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user = NULL
    event_data = Event.objects.get(pk=request.GET["eventID"])
    all_bookings = Booking.objects.all()
    for b in all_bookings:
        if event_data.id == b.event.id:
            if hasattr(event_data, 'avail_seats'):
                event_data.avail_seats -= b.seats

            else:
                event_data.avail_seats = event_data.seats - b.seats
    if not hasattr(event_data, "avail_seats"):
        event_data.avail_seats = event_data.seats
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        Booking.objects.create(event=event_data, user=current_user, seats=request.POST['seats'])
        messages.success(request, "Successful Booking")
    context = {
        "Event": event_data,
        "current_user": current_user,
        "form": form
    }
    return render(request, 'booking.html', context)


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
    context = {'form': form}
    return render(request, 'register.html', context)


def login_form(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username=username, password=password)

        if auth:
            if auth.is_active:
                login(request, auth)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        auth_form = AuthenticationForm()
        context = {'form': auth_form}
        return render(request, 'login.html', context)


def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/login')


def book(eventID):
    print(eventID)
    return HttpResponseRedirect('booking', event_id=eventID)


def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user = NULL
    all_bookings = Booking.objects.all()
    booked_events = []
    booked_seats = {}
    cake = UserLabelForm()
    #user_data = CustomUserChangeForm()
    if request.method == 'POST':
        cake = UserLabelForm(request.POST)
        #user_data = CustomUserChangeForm(UsernameField)
        UserLabel.objects.create(user=current_user,birthdate=request.POST["birthday"])
        messages.success(request, "Thank you")
    for bookingData in all_bookings:
        if bookingData.user.id == current_user.id:
            if hasattr(booked_seats, str(bookingData.event.id)):
                booked_seats[str(bookingData.event.id)] += bookingData.seats
            else:
                booked_seats[str(bookingData.event.id)] = bookingData.seats
            if bookingData.event not in booked_events:
                booked_events.append(bookingData.event)
    context = {
        #'user_form': user_data,
        'booked_events': booked_events,
        'cake': cake,
        'booked_seats': booked_seats,
        'current_user': current_user
    }
    return render(request, 'profile.html', context)
