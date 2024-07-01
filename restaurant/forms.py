from django import forms
from .models import reservatie # Ensure Review is imported from models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import UserProfile

class ReservatieForm(forms.ModelForm):
    class Meta:
        model = reservatie
        fields = ['voornaam', 'achternaam','email','aantal_pers','res_date']  # Fields from your Review model
        widgets = {
            'res_date': forms.DateInput(attrs={'type': 'date'}),
            'res_time': forms.TimeInput(attrs={'type': 'time'}),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            
        }