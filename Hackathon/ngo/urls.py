from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='ngo-home'), 
    path('register', views.ngo_register, name='ngo-register'), 
    path('login', views.ngo_login, name='ngo-login'), 
    path('logout/',auth_views.LogoutView.as_view(template_name='ngo/logout.html'),name="ngo-logout"), 
    path('eventlist/',views.eventlist, name='event-list')
]