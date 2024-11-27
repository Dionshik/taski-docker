"""Trebuet."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Trebuet."""

    class Meta:
        """Trebuet."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
