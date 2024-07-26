from rest_framework.routers import DefaultRouter

from tasks.views import TaskAPI

router = DefaultRouter()
router.register('tasks', TaskAPI, 'api_tasks')

urlpatterns = router.urls