from django.contrib import admin
from .models import Task


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title","user"]

admin.site.register(Task,TodoAdmin)