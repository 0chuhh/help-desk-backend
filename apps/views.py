import django_filters
from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from .models import *
from .serializers import *
from rest_framework.decorators import action
from .permissions import IsOwnerOrAdmin
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'delete':
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        if self.action == 'update':
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'delete':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'delete':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class ImportanceParametersView(viewsets.ModelViewSet):
    queryset = ImportanceParameters.objects.all()
    serializer_class = ImportanceParametersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'delete':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class TaskParametersView(viewsets.ModelViewSet):
    queryset = TaskParameters.objects.all()
    serializer_class = TaskParametersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class TaskCommentView(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def by_task(self, request, pk=None):
        queryset = TaskComment.objects.all()
        files = get_list_or_404(queryset, task_id=pk)
        serializer = TaskCommentSerializer(files, many=True)
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'delete':
    #         permission_classes = [IsOwnerOrAdmin]
    #     if self.action == 'update':
    #         permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]


class TaskCommentFileView(viewsets.ModelViewSet):
    queryset = TaskCommentFile.objects.all()
    serializer_class = TaskCommentFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def by_comment(self, request, pk=None):
        queryset = TaskCommentFile.objects.all()
        files = get_list_or_404(queryset, comment_id=pk)
        serializer = TaskCommentFileSerializer(files, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'delete':
            permission_classes = [IsOwnerOrAdmin]
        if self.action == 'update':
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
# Create your views here.
