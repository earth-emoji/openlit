from django.urls import include, path

from . import views

urlpatterns = [
    path('characters/', include(([
        path('<int:pk>/', views.creator_characters, name='my-characters'),
        path('create/', views.create_character, name="create"),
    ], 'characters'), namespace='characters')),
]