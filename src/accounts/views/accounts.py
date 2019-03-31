from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from accounts.forms import UserSignUpForm
from accounts.models import UserProfile
from users.models import User

# Create your views here.

class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'auth/signup_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile:wall', user.profile.id)


def signup_success(request, template_name='auth/success.html'):
    return render(request, template_name)

def logout_view(request):
    logout(request)
    return redirect('home')