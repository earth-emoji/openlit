from django.db import models

from accounts.models import UserProfile

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_id/<filename>
    return '{0}/{1}'.format(instance.user.username, filename)

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    file = models.ImageField(upload_to='photos/%Y/%m/%d/')
    default = models.BooleanField(default=False)
    cover = models.BooleanField(default=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.url)