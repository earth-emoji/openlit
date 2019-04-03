import simplejson as json
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StoryForm, ActForm, SceneForm, DialogueForm
from .models import Story, StoryCharacter, Act, Scene, Dialogue
from accounts.models import UserProfile
from characters.models import Character
from photos.models import Album, Photo

def author_stories(request, pk, template_name='stories/index.html', data={}):
    author = UserProfile.objects.get(pk=pk, user=request.user)
    stories = Story.objects.filter(author=author)
    data['stories'] = stories
    data['section'] = 'Story'
    return render(request, template_name, data)

def create_story(request, template_name='stories/story_form.html', data={}):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.author = request.user.profile
            album = Album.objects.create(name=c.title, owner=request.user.profile)
            photo = Photo.objects.create(file=form.cleaned_data['photo'], default=True, album=album)
            c.album = album
            c.save()
            return redirect('stories:my-stories', request.user.profile.id)
    else:
        form = StoryForm()
    data['form'] = form
    data['section'] = 'Story'
    return render(request, template_name, data)

def story_details(request, pk, template_name='stories/story_details.html', data={}):
    story = Story.objects.get(pk=pk, author=request.user.profile)
    characters = StoryCharacter.objects.filter(story=story)
    data['story'] = story
    data['characters'] = characters
    data['section'] = 'StoryDetails'
    return render(request, template_name, data)

def story_characters(request, pk, template_name='stories/story_characters.html', data={}):
    story = Story.objects.get(pk=pk, author=request.user.profile)
    data['story'] = story
    data['section'] = 'StoryDetails'
    return render(request, template_name, data)

def author_characters(request, pk, template_name='stories/author_characters.html', data={}):
    story = Story.objects.get(pk=pk, author=request.user.profile)
    story_characters = StoryCharacter.objects.filter(story=story).values('character')
    characters = Character.objects.filter(creator=request.user.profile).exclude(pk__in=story_characters)

    data['characters'] = characters
    data['story'] = story
    data['section'] = 'StoryDetails'
    return render(request, template_name, data)

@transaction.atomic
def assign_character(request, pk):

    if request.method == 'POST':
        character_id = request.POST['character']
        role = request.POST['role']

        character = Character.objects.get(pk=character_id)
        story = Story.objects.get(pk=pk, author=request.user.profile)

        story_character = StoryCharacter.objects.create(character=character, story=story, role=role)

        message = "%s has been assigned to %s" %(character.name, story.title)
        data = {'message': message}
        return JsonResponse(data)
    # return response
    return HttpResponse('')

def act_list(request, pk, template_name='stories/act_list.html', data={}):
    story = Story.objects.get(pk=pk)
    acts = Act.objects.filter(story=story).order_by('-act_number')
    data['story'] = story
    data['acts'] = acts
    data['section'] = 'StoryDetails'
    return render(request, template_name, data)

def act_create(request, pk, template_name='stories/act_form.html', data={}):
    story = Story.objects.get(pk=pk)
    form = ActForm(request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)
        c.story = story
        c.save()
        return redirect('stories:act-list', story.id)
    data['story'] = story
    data['form'] = form
    data['section'] = 'StoryDetails'
    return render(request, template_name, data)

def act_details(request, pk, template_name='stories/act_details.html', data={}):
    act = Act.objects.get(pk=pk)
    scenes = Scene.objects.filter(act=act).order_by('-position')
    data['act'] = act
    data['scenes'] = scenes
    data['section'] = 'Act'
    return render(request, template_name, data)

def scene_create(request, pk, template_name='stories/scene_form.html', data={}):
    act = Act.objects.get(pk=pk)
    form = SceneForm(request.POST or None)

    if form.is_valid():
        c = form.save(commit=False)
        c.act = act
        c.save()
        return redirect('stories:act-view', act.id)
    data['form'] = form
    data['act'] = act
    data['section'] = 'Act'
    return render(request, template_name, data)

def scene_details(request, pk, template_name='stories/scene_details.html', data={}):
    scene = Scene.objects.get(pk=pk)
    act = Act.objects.get(pk=scene.act.id)
    data['act'] = act
    data['scene'] = scene
    data['section'] = 'Act'
    return render(request, template_name, data)