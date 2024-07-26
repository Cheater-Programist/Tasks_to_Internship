from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from tasks.serializers import TaskSerializer
from tasks.models import Task

# Create your views here.
class TaskAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer