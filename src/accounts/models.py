import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(models.Manager):
    use_for_related_fields = True

# Create your models here. 
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    contacts = models.ManyToManyField('self', related_name='contacts', blank=True)

    objects = UserProfileManager()

    def __str__(self):
        return self.user.username

class ContactRequest(models.Model):
    # user requesting
    sender = models.ForeignKey(UserProfile, related_name='requests_sent', on_delete=models.CASCADE)
    
    # user requested
    receiver = models.ForeignKey(UserProfile, related_name='requests_received' , on_delete=models.CASCADE)
    
    # status
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Follow(models.Model):
    followed = models.ForeignKey(UserProfile, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(UserProfile, related_name='followed_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)