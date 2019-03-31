from django.db import models

from accounts.models import UserProfile

# Create your models here.
class Post(models.Model):
    
    content = models.TextField()

    author = models.ForeignKey(UserProfile, related_name='user_post', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    # @property
    # def get_comment(self):
    #     return self.post_comment.all().order_by('created_at')
