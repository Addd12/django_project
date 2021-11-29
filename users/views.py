from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # request.post to pass the post data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile') # if u're not redirected it will give the message "are u sure u want to reload" becase it's post data thet is or should be filled, or u should run another post request
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    #to pass the created forms to the template, use context 
    context = {
        'u_form': u_form, 
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
