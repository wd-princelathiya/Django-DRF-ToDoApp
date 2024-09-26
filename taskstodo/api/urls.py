from rest_framework.routers import DefaultRouter
from .views import TasksToDoView

router = DefaultRouter()
router.register("taskstodo", TasksToDoView, basename="task_list")

urlpatterns = []

urlpatterns += router.urls
