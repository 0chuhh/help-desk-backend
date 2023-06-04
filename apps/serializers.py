from rest_framework import serializers
from .models import *


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
        fields = '__all__'