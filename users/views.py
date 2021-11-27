from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #UserCreationForm was the previous (default) one which didn't have the email field
        if form.is_valid():
            form.save() #this is the line that actually saves the user to the db
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm() #UserCreationForm was here as well
    return render(request, 'users/register.html', {'form': form})
