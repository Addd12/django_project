from django import forms 
from django. contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # bcs whenever the form validates it creates a new user
        fields = ['username', 'email', 'password1', 'password2'] # the fields that are here will be the ones in our form, in the written order!!! 
