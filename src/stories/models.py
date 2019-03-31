from django.db import models

from accounts.models import UserProfile
from characters.models import Character
from photos.models import Album

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=255)
    premise = models.CharField(max_length=300, null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stories')
    characters = models.ManyToManyField(Character, through='StoryCharacter', blank=True)

    def __str__(self):
        return self.title

class StoryCharacter(models.Model):
    ROLE_CHOICE_TYPES = (
        ('Protagonist', 'Protagonist'),
        ('Deuteragonist', 'Deuteragonist'),
        ('Antagonist', 'Antagonist'),
        ('Love Interest', 'Love Interest'),
        ('Mentor', 'Mentor'),
        ('Narrator', 'Narrator'),
        ('Secondary', 'Secondary Character'),
        ('Tertiary', 'Tertiary Character'),
        ('Flat', 'Flat Character'),
    )

    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='stories')
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICE_TYPES)

class Act(models.Model):
    act_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='acts')

    def __str__(self):
        return self.title

class Scene(models.Model):
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=255, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    weather = models.CharField(max_length=255, null=True, blank=True)
    setup = models.TextField(null=True, blank=True)
    action = models.TextField(null=True, blank=True)
    position = models.PositiveIntegerField()
    act = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='scenes')
    characters = models.ManyToManyField(Character, related_name='scenes', blank=True)

    def __str__(self):
        return self.title

class Dialogue(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name='dialogues')
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='dialogues')
    content = models.TextField()