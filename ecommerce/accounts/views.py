from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import LoginForm


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')    
        else:
            messages.error(request, "Account creation failed")
            return render(request, 'accounts/register.html', {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'accounts/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username  = authenticate(request, username = data['username'], password = data['password'])
            if username is not None:
                login(request, username)
                return redirect('/dashboard')
            else:
                messages.error(request, 'Invalid username or passwrod')
                return render(request, 'accounts/login.html', {'form': form})
        else:
            messages.error(request, 'Invalid username or passwrod')
            return render(request, 'accounts/login.html', {'form': form})

    context = {
        'form' : LoginForm
    }
    return render(request, 'accounts/login.html', context)


def dashboard(request):
    return render(request, 'accounts/dashboard.html')