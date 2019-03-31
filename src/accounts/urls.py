from django.urls import include, path

from .views import accounts, profile
from posts import views as posts

urlpatterns = [
    path('logout/', accounts.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.UserSignUpView.as_view(), name='user_signup'),
    path('accounts/signup/success/', accounts.signup_success, name='success'),
    path('profile/', include(([
        path('<int:pk>/', posts.wall, name='wall'),
        path('<int:pk>/posts/', posts.timeline, name='timeline'),
        path('load-posts/', posts.load_posts, name='load-posts'),
    ], 'accounts'), namespace='profile')),
    path('community/', include(([
        path('', profile.people_list, name='people'),
    ], 'accounts'), namespace='community')),
    path('contacts/', include(([
        path('<int:pk>/', profile.contacts_list, name='pro_contacts'),
        path('<int:pk>/send-request', profile.send_contact_request, name='send_request'),
        path('<int:pk>/contact-requests', profile.contact_requests, name='contact_requests'),
        path('<int:pk>/contact-response', profile.contact_response, name='contact_response'),
    ], 'accounts'), namespace='contacts')),
]