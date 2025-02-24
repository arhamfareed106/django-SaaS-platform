from dataclasses import field
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user= form.save()
            authenticate(username=user.username, password=user.password)
            
            if user is not None:
                login(request, user)
                return redirect('/')

            
    else:
        form = SignupForm()
    return render(request, 'user/signup.html',{
        'form': form,
    })

