from django.db import models

from accounts.models import UserProfile

# Create your models here.
class SocialGroup(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(UserProfile, through='Membership', blank=True)
    founder = models.ForeignKey(UserProfile, related_name="social_groups", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def get_member_count(self):
        return self.members.all().count()

class Membership(models.Model):
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    group = models.ForeignKey(SocialGroup, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

class GroupRequest(models.Model):
    group = models.ForeignKey(SocialGroup, related_name='group_requests', on_delete=models.CASCADE)
    REQUEST_TYPE_CHOICES = (
        ('GROUP_INVITE', 'GROUP INVITE'),
        ('USER_INQUIRY', 'USER INQUIRY'),
    )
    prospect = models.ForeignKey(UserProfile, related_name='group_prospects', on_delete=models.CASCADE)
    request_type = models.CharField(max_length=12, choices=REQUEST_TYPE_CHOICES)
    status = models.BooleanField(default=False)