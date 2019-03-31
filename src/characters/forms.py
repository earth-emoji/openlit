from django import forms
from django.db import transaction
from .models import Character
from accounts.models import UserProfile

class CharacterForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    #recipients = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    # published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Character
        fields = ['name', 'photo']