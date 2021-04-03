from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NgoSignUpForm
from django.contrib import messages

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
