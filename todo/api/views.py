from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView

from todo.api.serializers import TaskItemSerializer
from todo.models import TaskItem


class TaskItemList(ListCreateAPIView):
    serializer_class = TaskItemSerializer
    queryset = TaskItem.objects.all()

class TaskItemDetail(RetrieveAPIView):
    serializer_class = TaskItemSerializer
    queryset = TaskItem.objects.all()
