from rest_framework.response import Response
from taskstodo.models import Task
from .serializer import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from accounts.models import User
from ..models import Task
from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.response import Response



class TasksToDoView(viewsets.ModelViewSet):
    """this is a class for get list of posts
    and a single post and also for create,
    edit and delete post"""

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """
        get option portfolio positions that
        belong to specific user from db
        """
        user = User.objects.get(id=self.request.user.id)
        queryset = Task.objects.filter(user=user)

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()

        return queryset
