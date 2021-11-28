from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #UserCreationForm was the previous (default) one which didn't have the email field
        if form.is_valid():
            form.save() #this is the line that actually saves the user to the db
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm() #UserCreationForm was here as well
    return render(request, 'users/register.html', {'form': form})

@login_required #this is a decorator - it adds functionality to an existing function, in this case requires login before accessing the profile page
def profile(request):
    return render(request, 'users/profile.html')
