from django import forms
from django.db import transaction
from .models import Message
from accounts.models import UserProfile

class MessageForm(forms.ModelForm):
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'rows':'3'}))
    #recipients = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    # published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Message
        fields = ['subject', 'body', 'recipients',]
        widgets = {
            'recipients' : forms.SelectMultiple(attrs={'class':'form-control'})
        }

    def __init__(self, user, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        profile = UserProfile.objects.get(user=user)
        self.fields['recipients'].queryset = profile.contacts.all()