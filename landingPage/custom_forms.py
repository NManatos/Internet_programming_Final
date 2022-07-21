from django import forms
from django.conf.global_settings import DATE_INPUT_FORMATS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserLabel
from django.forms.widgets import DateTimeInput
from django.forms import ModelForm


# from django.contrib.admin import ModelAdmin
# from fieldmaker.forms import ExpandableForm

class mDateTimeField(forms.DateTimeField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('input_formats', DATE_INPUT_FORMATS)
        super(mDateTimeField, self).__init__(*args, **kwargs)


class CustomUserChangeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)


class UserLabelForm(forms.Form):
    birthday = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))



class BookingForm(forms.Form):
    seats = forms.IntegerField(max_value=10, min_value=0)


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': ("Please enter a correct %(username)s and password."
                          "Note that both fields may be case-sensitive."),
        'inactive': ("This account is inactive"),
    }


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
