from django.urls import include, path

from . import views

urlpatterns = [
    path('stories/', include(([
        path('creator/<int:pk>/', views.author_stories, name='my-stories'),
        path('create/', views.create_story, name="create"),
        path('<int:pk>/view', views.story_details, name='view'),
        path('<int:pk>/characters', views.story_characters, name='story-characters'),
        path('<int:pk>/author-characters', views.author_characters, name='author-characters'),
        path('<int:pk>/character-assignment/', views.assign_character, name='assign-character'),
        path('<int:pk>/acts/', views.act_list, name='act-list'),
        path('<int:pk>/act-create/', views.act_create, name='act-create'),
    ], 'stories'), namespace='stories')),
]