from django.urls import path, include

app_name = "taskstodo"

urlpatterns = [path("api/", include("taskstodo.api.urls"))]
