from django.conf import settings
from django.db import models

from accounts.models import UserProfile

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    sender = models.ForeignKey(UserProfile, related_name='messages_sent', on_delete=models.CASCADE)
    recipients = models.ManyToManyField(UserProfile, related_name='messages_recieved')
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.user.email + ": " + self.subject
    