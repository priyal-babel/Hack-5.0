from django.shortcuts import render
from django.http import HttpResponseRedirect, request

def contact(request):
    return render(request,'ngo/contactus.html')