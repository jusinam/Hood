from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField
from .models import Neighbourhood, Profile, Business, Post


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user','neighbourhood')


