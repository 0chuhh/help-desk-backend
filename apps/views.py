import django_filters
from django.shortcuts import render
from rest_framework import permissions, viewsets, generics, mixins
from .models import *
from rest_framework import status
from .serializers import *
from rest_framework.decorators import action
from .permissions import IsOwnerOrAdmin
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token


class UsersView(mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        try:
            user = request.user
            token = Token.objects.get(user=user)
            groups = GroupSerializer(request.user.groups.all(), many=True)
            try:
                image = UsersImage.objects.get(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email,
                    'username': user.username,
                    'isStaff':user.is_staff,
                    'roles': groups.data,
                    'image': image.image.url
                })
            except:
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email,
                    'isStaff':user.is_staff,
                    'username': user.username,
                    'roles': groups.data,
                })

        except:
            return Response('Не авторизован',status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['post'])
    def signUp(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                email=serializer.data['email'],
                username=serializer.data['username'],
                password=serializer.data['password']
            )
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username': user.username
            }, status=status.HTTP_201_CREATED)
        return Response('error')
    
    def get_permissions(self):
        if self.action == 'delete':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'me':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]



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


class ResolvedTasksView(viewsets.ModelViewSet):
    pass



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
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def by_task(self, request, pk=None):
        queryset = TaskComment.objects.all()
        files = get_list_or_404(queryset, task_id=pk)
        serializer = TaskCommentSerializer(files, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'delete':
            permission_classes = [IsOwnerOrAdmin]
        if self.action == 'update':
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


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


class TaskFileView(viewsets.ModelViewSet):
    queryset = TaskFile.objects.all()
    serializer_class = TaskFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def by_task(self, request, pk=None):
        queryset = TaskCommentFile.objects.all()
        files = get_list_or_404(queryset, task_id=pk)
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


class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action == 'list':
            return FAQSerializer
        return FAQDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'delete':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    

class FAQFilesView(viewsets.ModelViewSet):
    queryset = FAQFiles.objects.all()
    serializer_class = FAQFilesSerializer
    permission_classes = []

    @action(detail=True, methods=['get','post'])
    def by_faq(self, request, pk=None):
        if request.method == 'GET':
            queryset = FAQFiles.objects.all()
            files = get_list_or_404(queryset, faq_id=pk)
            serializer = FAQFilesSerializer(files, many=True)
        if request.method == 'POST':
            serializer = FAQFilesSerializer(data=request.data, many=True)
            if serializer.is_valid():
                if len(serializer.data)>1:
                    for item in serializer.data:
                        FAQFiles(*item)
                        FAQFiles.save()
                print(request.data)
                print('HUI')
                # FAQFiles.objects.create(**serializer.data)
        return Response(serializer.data)


    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        if self.action == 'delete':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
# Create your views here.
