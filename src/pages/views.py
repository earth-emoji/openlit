from django.shortcuts import render, redirect

# Create your views here.
def home(request, template_name='pages/home.html', data={}):
    if request.user.is_authenticated:
        return redirect('profile:wall', request.user.profile.id)
    return render(request, template_name, data)