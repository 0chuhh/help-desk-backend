from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import InMemoryUploadedFile


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    image = serializers.ImageField(required=False)
    groups = GroupSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = User
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ImportanceParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportanceParameters
        fields = '__all__'


class TaskParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskParameters
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'


class TaskCommentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCommentFile
        fields = '__all__'


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id','name','description', 'type', 'resolved_task')


class FAQDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id','name','description', 'type', 'resolved_task', 'html')


class FAQFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQFiles
        fields = '__all__'