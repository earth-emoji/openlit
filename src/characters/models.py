from django.db import models

from accounts.models import UserProfile
from photos.models import Album

# Create your models here.
class Character(models.Model):

    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=30, null=True, blank=True)
    age = models.CharField(max_length=9, null=True, blank=True)
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    sexual_preference = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    income = models.CharField(max_length=9, null=True, blank=True)
    abilities = models.TextField(blank=True, null=True)
    relationship_skills = models.TextField(blank=True, null=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, null=True, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='characters')

class CharacterAppearance(models.Model):
    height = models.CharField(max_length=10, null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    race = models.CharField(max_length=20, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    skin_color = models.CharField(max_length=20, null=True, blank=True)
    face_shape = models.TextField(null=True, blank=True)
    distinguishing_features = models.TextField(null=True, blank=True)
    mannerism = models.TextField(null=True, blank=True)
    habits = models.TextField(null=True, blank=True)
    health = models.TextField(null=True, blank=True)
    speech_patterns = models.CharField(max_length=20, null=True, blank=True)
    disabilities = models.TextField(null=True, blank=True)
    style = models.CharField(max_length=255, null=True, blank=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)


class CharacterPsychology(models.Model):
    ATTITUDE_TYPE_CHOICES = (
        ('Extravert', 'Extravert'),
        ('Introvert', 'Introvert')
    )

    intelligence_level = models.CharField(max_length=255, null=True, blank=True)
    mental_illnesses = models.TextField(null=True, blank=True)
    learning_experiences = models.TextField(null=True, blank=True)
    short_term_goals = models.TextField(null=True, blank=True)
    long_term_goals = models.TextField(null=True, blank=True)
    self_perception = models.TextField(null=True, blank=True)
    perceived_by_others = models.TextField(null=True, blank=True)
    self_confidence = models.CharField(max_length=255, null=True, blank=True)
    emotionality = models.TextField(null=True, blank=True)
    shame = models.TextField(null=True, blank=True)
    mental_strengths =  models.TextField(null=True, blank=True)
    mental_weaknesses =  models.TextField(null=True, blank=True)
    attitude_type = models.CharField(max_length=15, choices=ATTITUDE_TYPE_CHOICES, null=True, blank=True)
    deals_with_anger = models.TextField(null=True, blank=True)
    deals_with_sadness = models.TextField(null=True, blank=True)
    deals_with_conflict = models.TextField(null=True, blank=True)
    deals_with_change = models.TextField(null=True, blank=True)
    deals_with_loss = models.TextField(null=True, blank=True)
    movations = models.TextField(null=True, blank=True)
    fears = models.TextField(null=True, blank=True)
    pleasures = models.TextField(null=True, blank=True)
    spiritual_beliefs = models.TextField(null=True, blank=True)
    extras = models.TextField(null=True, blank=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE)

class CharacterRelationship(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='relations')
    relation = models.ForeignKey(Character, on_delete=models.CASCADE)
    description = models.TextField()

