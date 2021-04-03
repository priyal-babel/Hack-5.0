from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from ngo.models import User, EventManager

class EventManagerSignUpForm(UserCreationForm):
    Organization_name = forms.CharField(required=True)
    manager_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)   
    state = forms.CharField(required=True) 
    city = forms.CharField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email', 'Organization_name', 'manager_name', 'phone_number', 'address', 'city', 'state', 'zipcode', 'password1', 'password2')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_eventManager = True
        user.name = self.cleaned_data.get('Organization_name')
        user.manager_name = self.cleaned_data.get('manager_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.state = self.cleaned_data.get('state')
        user.city = self.cleaned_data.get('city')
        user.save()
        event_manager = EventManager.objects.create(user=user)
        event_manager.save()
        return user