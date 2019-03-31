from django.urls import include, path

from . import views

urlpatterns = [
    path('files/', include(([
        path('', views.files_home_view, name="files_home"),
        path('download/', views.download_view, name="download_file"),
    ], 'files'), namespace='files')),
]