from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventManagerSignUpForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'eventManager/home.html')

def organizer_register(request):
    if request.method == 'POST':
        form = EventManagerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('event-home')
    else:
        form = EventManagerSignUpForm()
    return render(request, 'eventManager/register.html', {'form': form})