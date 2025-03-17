from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/register')    
        else:
            messages.error(request, "Account creation failed")
            return render(request, 'accounts/register.html', {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'accounts/register.html', context)