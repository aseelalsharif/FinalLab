from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #this to create a new user
from django.contrib import messages
from . forms import SignUpForm
# Create your views here.

def SignUp(request): 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():#check is_vaild function
            form.save()
            FristName = form.cleaned_data.get('first_name')
            messages.success(request, f'Hi {FristName}, your account created')
            return redirect('Login')
    else:
        form = SignUpForm()
    return render(request, 'register/SignUp.html',{'SignUpForm': form})

def Profile(request):
    return render(request, 'register/UserProfile.html')
