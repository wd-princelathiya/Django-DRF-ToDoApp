from django.urls import path, include
from . import views

app_name = "taskstodo"

urlpatterns = [
    path("api/", include("taskstodo.api.urls"))
]