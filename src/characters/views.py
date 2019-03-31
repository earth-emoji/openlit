from django.shortcuts import render, redirect

from .forms import CharacterForm
from .models import Character
from accounts.models import UserProfile
from photos.models import Album, Photo

# Create your views here.

def creator_characters(request, pk, template_name='characters/index.html', data={}):
    creator = UserProfile.objects.get(pk=pk, user=request.user)
    characters = Character.objects.filter(creator=creator)
    data['characters'] = characters
    data['section'] = 'Characters'
    return render(request, template_name, data)

def create_character(request, template_name='characters/character_form.html', data={}):
    
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.creator = request.user.profile
            album = Album.objects.create(name=c.name, owner=request.user.profile)
            photo = Photo.objects.create(file=form.cleaned_data['photo'], default=True, album=album)
            c.album = album
            c.save()
            return redirect('characters:my-characters', request.user.profile.id)
    else:
        form = CharacterForm()
    data['form'] = form
    return render(request, template_name, data)