from datetime import datetime, timedelta
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone

from accounts.models import UserProfile

# Create your models here.


class Folder(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='folders')

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=500, null=True)
    file_type = models.CharField(max_length=100, null=True)
    size = models.IntegerField(null=True)
    file = models.FileField(upload_to='docs')
    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name='files', null=True, blank=True)

    def __str__(self):
        return self.name

class Share(models.Model):
    message = models.CharField(max_length=255, null=True, blank=True)
    sender = models.ForeignKey(
        UserProfile, related_name='files_shared', on_delete=models.CASCADE)
    recipients = models.ManyToManyField(
        UserProfile, related_name='files_recieved')
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='share_history')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def pre_save_file_info(sender, instance, *args,**kwargs):
    instance.location = instance.file.url
    instance.size = instance.file.size

pre_save.connect(pre_save_file_info, sender=File)