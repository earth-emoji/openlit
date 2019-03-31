from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from users.decorators import group_required
from users.models import User
from accounts.models import UserProfile, ContactRequest

@login_required
def user_profile(request, pk, template_name='accounts/profile/index.html'):
    profile = get_object_or_404(UserProfile, pk=pk, user=request.user)
    data = {}
    data['profile'] = profile
    return render(request, template_name, data)

@login_required
def people_list(request, template_name='accounts/profile/people.html'):
    # get list of all users
    people = UserProfile.objects.exclude(user=request.user)
    # set up data context
    data = {}
    data['people'] = people
    
    return render(request, template_name, data)

@login_required
def send_contact_request(request, pk):
    # get current user (befriender)
    profile = UserProfile.objects.get(pk=pk)

    # get user that is being befriended
    if request.method == 'POST':
        contact = request.POST['contact']

        contact_profile = UserProfile.objects.get(pk=contact)

        # create a friendship
        contact_request = ContactRequest.objects.create(sender=profile, receiver=contact_profile)
    # return response
    return HttpResponse('')

@login_required
def contact_requests(request, pk, template_name='contacts/contact_requests.html'):
    # get list of user contact requests
    user = get_object_or_404(UserProfile, pk=pk, user=request.user)
    requests = ContactRequest.objects.filter(receiver=user, status=False)

    data = {}

    data['requests'] = requests

    return render(request, template_name, data)

@login_required
@transaction.atomic
def contact_response(request, pk):
    current_user = UserProfile.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        status = int(request.POST['status'])
        contact = request.POST['contact']
        sender = UserProfile.objects.get(pk=contact)

        # get request
        contact_request = ContactRequest.objects.get(sender=sender, receiver=current_user)

        # update request
        if (status == 1):
            contact_request.status = status
            contact_request.save()
            current_user.contacts.add(sender)
            sender.contacts.add(current_user)
     # return response
    return HttpResponse('')


@login_required
def contacts_list(request, pk, template_name='contacts/contacts_list.html'):
    profile = UserProfile.objects.get(pk=pk)
    data = {}
    data['pro'] = profile
    return render(request, template_name, data)


