"""Trebuet."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """123."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
