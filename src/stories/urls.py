from django.urls import include, path

from . import views

urlpatterns = [
    path('', include(([
        path('stories/creator/<int:pk>/', views.author_stories, name='my-stories'),
        path('stories/create/', views.create_story, name="create"),
        path('stories/<int:pk>/view', views.story_details, name='view'),
        path('stories/<int:pk>/characters', views.story_characters, name='story-characters'),
        path('stories/<int:pk>/author-characters', views.author_characters, name='author-characters'),
        path('stories/<int:pk>/character-assignment/', views.assign_character, name='assign-character'),
        path('stories/<int:pk>/acts/', views.act_list, name='act-list'),
        path('stories/<int:pk>/act-create/', views.act_create, name='act-create'),
        path('acts/<int:pk>/', views.act_details, name='act-view'),
        path('act/<int:pk>/scene-create/', views.scene_create, name='scene-create'),
        path('scenes/<int:pk>/', views.scene_details, name='scene-view'),
    ], 'stories'), namespace='stories')),
]