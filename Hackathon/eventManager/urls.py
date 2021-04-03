from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'), 
    path('register', views.organizer_register, name='event-register'), 
]