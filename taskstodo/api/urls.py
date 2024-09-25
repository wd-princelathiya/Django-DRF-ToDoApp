from rest_framework.routers import DefaultRouter
from .views import TasksToDoView

router = DefaultRouter()
router.register("taskstodo", TasksToDoView, basename="task_list")
# router.register(
#     "task-detail",
#     TodoDetailApiView,
#     basename="task_detail",
# )

urlpatterns = []

urlpatterns += router.urls