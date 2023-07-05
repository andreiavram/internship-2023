from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo.api.filters import TaskFilter, DocumentFilter
from todo.api.permissions import SuperuserPermission
from todo.api.serializers import TaskItemSerializer, UserSerializer, DocumentSerializer
from todo.models import TaskItem, Document


class TaskItemViewSet(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer
    permission_classes = [IsAuthenticated, SuperuserPermission]
    filterset_class = TaskFilter

    @action(detail=True, methods=['patch'])
    def set_done(self, request, pk=None):
        task = TaskItem.objects.get(id=pk)
        task.status = TaskItem.TaskItemStatuses.DONE
        task.save()
        serializer = self.serializer_class(task)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, ]
    filterset_class = DocumentFilter


