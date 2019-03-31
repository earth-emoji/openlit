import simplejson as json
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse

from .forms import PostForm
from .models import Post
from accounts.models import UserProfile, Follow

# Create your views here.
def wall(request, pk):
    if not(request.user.is_authenticated):
        redirect('home')

    user = UserProfile.objects.get(pk=pk, user=request.user)
    followed = Follow.objects.filter(follower=user).values('followed')
    posts = Post.objects.filter(Q(author=user) | Q(author__id__in=followed)).order_by('-created_at')
    form = PostForm(request.POST or None)
    users = UserProfile.objects.all()

    if form.is_valid():
        c = form.save(commit=False)
        c.user = user
        c.save()
        return redirect('profile:wall', user.id)
    
    data = {
        'posts': posts,
        'form': form,
        'users': users,
        'section': 'Wall'
    }

    return render(request, 'posts/wall.html', data)

def timeline(request, pk):
    if not(request.user.is_authenticated):
        redirect('home')
    user = UserProfile.objects.get(pk=pk, user=request.user)
    posts = Post.objects.filter(author=user)
    form = PostForm(request.POST or None)

    if form.is_valid():
        c = form.save(commit=False)
        c.author = user
        c.save()
        return redirect('profile:wall', user.id)
    
    data = {
        'posts': posts,
        'form': form
    }

    return render(request, 'posts/timeline.html', data)

@login_required
def load_posts(request):
    if request.method == 'GET': 
        user_id = int(request.GET['user_id'])
        user = UserProfile.objects.get(pk=user_id)
        followed = Follow.objects.filter(follower=user).values('followed')
        posts = Post.objects.filter(Q(author=user) | Q(author__id__in=followed)).order_by('-created_at')
        data = serializers.serialize('json', posts)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse('')