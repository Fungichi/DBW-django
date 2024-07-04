from django import forms
from .models import reservatie # Ensure Review is imported from models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import UserProfile

class ReservatieForm(forms.ModelForm):
    class Meta:
        model = reservatie
        fields = ['voornaam', 'achternaam','email','aantal_pers','res_date','res_time']  # Fields from your Review model
        widgets = {
            'res_date': forms.DateInput(attrs={'type': 'date'}),
            'res_time': forms.TimeInput(attrs={'type': 'time'}),
            'email': forms.EmailInput(attrs={'type': 'email'}),
            
        }

from .models import review  # Ensure Review is imported from models
#from .models import UserProfile

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ['text', 'stars']  # Fields from your Review model
        widgets = {
            'text': forms.Textarea(attrs={'cols': 20, 'rows': 10}),  # Customize the size of the textarea
        }