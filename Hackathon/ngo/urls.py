from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='ngo-home'), 
    path('register', views.ngo_register, name='ngo-register'), 
]