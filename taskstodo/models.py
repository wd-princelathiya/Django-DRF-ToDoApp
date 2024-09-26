from django.db import models
from accounts.models import User

# Create your models here.


class Task(models.Model):

    title = models.CharField(max_length=256)
    comments = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
