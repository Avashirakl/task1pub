from dataclasses import field, fields
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, TaskChanging, Notification


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'author', 'status', 'start_date', 'end_date']


class TaskChangingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskChanging
        fields = ['task', 'prevstatus', 'currentstatus','changed_by',]


class NotificationSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['users', 'task', 'created_at',]
