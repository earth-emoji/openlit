from django.shortcuts import render, redirect, get_object_or_404

from .models import Message
from .forms import MessageForm
from accounts.models import UserProfile

# Create your views here.
def inbox(request, pk, template_name='private_messages/inbox.html'):
    # get the current user
    user = UserProfile.objects.get(pk=pk)
    # get a list of messages that the current user is the receipent of
    messages = Message.objects.filter(recipients=user)
    data = {}
    data['messages'] = messages
    return render(request, template_name, data)

def outbox(request, pk, template_name='private_messages/outbox.html'):
    # get the current user
    user = UserProfile.objects.get(pk=pk)
    # get a list of messages that the current user is the receipent of
    messages = Message.objects.filter(sender=user)
    data = {}
    data['messages'] = messages
    return render(request, template_name, data)

def compose(request, template_name='private_messages/message_form.html'):
    form = MessageForm(request.user, request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)
        c.sender = request.user.profile
        c.save()
        form.save_m2m()
        return redirect('messages:inbox', request.user.profile.id)
    return render(request, template_name, {'form': form})

def message_details(request):
    pass