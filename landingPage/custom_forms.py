from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RatingForm(forms.Form):
    rating =forms.IntegerField()        
class BookingForm(forms.Form):
    seats = forms.IntegerField(max_value=10,min_value=0)
    
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

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )
        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name']
        user.save() 
        return user 