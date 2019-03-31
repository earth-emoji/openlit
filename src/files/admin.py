from django.contrib import admin

from .models import File, Folder

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    pass
    # fields = ["name","uploaded_at", "expires_at", "urlname", "duration"]
    # list_display = ["name", "uploaded_at", "duration",  "expires_at", "urlname", "file_link"]

admin.site.register(File)
admin.site.register(Folder)