from django import forms

class FileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'custom-file-input'}))