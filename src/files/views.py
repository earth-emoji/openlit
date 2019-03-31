from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.conf import settings

from .models import File, Folder

import os

file_content_types = [
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/msword',
    'application/vnd.ms-powerpoint',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.oasis.opendocument.presentation',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.oasis.opendocument.text',
    'application/epub+zip',
    'application/pdf',
    'text/csv',
    'text/plain',
]


def files_home_view(request):
    context = {}
    context["folders"] = Folder.objects.filter(creator=request.user.profile).exclude(name="Shared")
    if request.method == 'POST':
        uploaded_file = request.FILES['my_file']
        folder = request.POST['folder']
        if uploaded_file.content_type not in file_content_types:
            print("INVALID CONTENT TYPE")

        else:
            new_file = File(file=uploaded_file,
                            file_type=uploaded_file.content_type)
            
            new_file.folder = Folder.objects.get(pk=folder)
            new_file.save()
            print(uploaded_file.content_type)

    qs = File.objects.all().order_by('-uploaded_at')
    context['files'] = qs

    context["file_types"] = file_content_types
    file_type_counts = []
    for file_type in file_content_types:
        count = File.objects.filter(file_type=file_type).count()
        file_type_counts.append(count)

    context["file_type_counts"] = file_type_counts

    return render(request, "files/index.html", context)


def download_view(request):
    if request.method == 'POST':
        path = request.POST.get('path')
        print(path)
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/force-download")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(file_path)
                return response
    raise Http404
