from taskstodo.models import Task
from .serializer import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from accounts.models import User
from django.db.models.query import QuerySet


class TasksToDoView(viewsets.ModelViewSet):
    """this is a class for get list of tasks
    and a single task and also for create,
    edit and delete tasks"""

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        get tasks that belong to specific user from db
        """
        user = User.objects.get(id=self.request.user.id)
        queryset = Task.objects.filter(user=user)

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()

        return queryset
