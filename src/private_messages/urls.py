from django.urls import include, path

from . import views

urlpatterns = [
    path('messages/', include(([
        path('<int:pk>/inbox/', views.inbox, name='inbox'),
        path('<int:pk>/outbox/', views.outbox, name='outbox'),
        path('compose/', views.compose, name='compose'),
    ], 'private_messages'), namespace='messages')),
]