from django.contrib.auth import get_user_model
from rest_framework import serializers

from todo.models import TaskItem, Document


class BaseDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["uploaded_file", "upload_time", "owner", "url"]

    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.uploaded_file.url

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["uploaded_file", "upload_time", "owner", "task"]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "full_name", "last_login", "email"]

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ['id', 'title', 'description', 'date_due', 'users', 'child_count', 'user_objects', 'documents', 'status']

    child_count = serializers.SerializerMethodField()
    user_objects = UserSerializer(source="users", many=True, read_only=True)
    documents = BaseDocumentSerializer(many=True)

    def get_child_count(self, obj):
        return obj.children.all().count()

