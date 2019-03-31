from django import forms
from django.db import transaction
from .models import Story, Act, Scene, Dialogue
from accounts.models import UserProfile

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    #recipients = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    # published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Story
        fields = ['title', 'photo']

class ActForm(forms.ModelForm):
    act_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control rounded-pill'}))
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))

    class Meta:
        model = Act
        fields = ['act_number', 'title']

class SceneForm(forms.ModelForm):
    position = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control rounded-pill'}))
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control rounded-pill'}))

    class Meta:
        model = Scene
        fields = ['position', 'title']

class DialogueForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'rows':'3'}))

    class Meta:
        model = Dialogue
        fields = ['content']
