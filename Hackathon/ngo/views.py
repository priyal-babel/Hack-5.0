from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NgoSignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'ngo/home.html')

def ngo_register(request):
    if request.method == 'POST':
        form = NgoSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('ngo-home')
    else:
        form = NgoSignUpForm()
    return render(request, 'ngo/register.html', {'form': form})

def ngo_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('ngo-home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'ngo/login.html',
    context={'form':AuthenticationForm()})

def eventlist(request):
    return render(request, 'ngo/eventList.html')