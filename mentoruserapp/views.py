from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView


def register(request):
    if request.method == 'POST':
        reg = RegistrationForm(request.POST)
        if reg.is_valid():
            reg.save()
            return redirect('login')
    else:
        reg = RegistrationForm()
    return render(request, 'register.html', {'form': reg})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        ob = authenticate(request, username=email,password=password)
        if ob:
            return HttpResponse('Login Successfull')
        else:
            return HttpResponse('Bad request Login Unsuccessfull')
    else:
        return render(request, 'login.html')