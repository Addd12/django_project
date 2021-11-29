from django import forms 
from django. contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # bcs whenever the form validates it creates a new user
        fields = ['username', 'email', 'password1', 'password2'] # the fields that are here will be the ones in our form, in the written order!!! 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] # let's the program know that we'll work with the username and password

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']