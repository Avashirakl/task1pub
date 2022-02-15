from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Notification
from blog.models.task import Task
from blog.models.taskchanging import TaskChanging


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'author', 'status', 'previousstatus', 'start_date', 'end_date', 'spectators', ]


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'previousstatus', 'start_date', 'end_date']


class TaskRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'author', 'status', 'previousstatus', 'start_date', 'end_date', 'spectators', ]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'author', 'spectators', 'status', 'previousstatus', 'changed_by', 'end_date', ]
        read_only_fields = ['id', 'name', 'description', 'author', 'spectators', 'previousstatus']

    def update(self, instance, validated_data):
        instance.previousstatus = instance.status
        varprev = instance.previousstatus
        instance.status = validated_data.get('status')
        varstat = instance.status
        TaskChanging.objects.create(task=instance,
                                    currentstatus=varstat,
                                    prevstatus=varprev,
                                    changed_by=validated_data.get('author', instance.author))
        return super().update(instance, validated_data)


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']


class TaskChangingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskChanging
        fields = ['id', 'task', 'currentstatus', 'prevstatus', 'changed_by', 'changed_at']


class NotificationSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'users', 'task', 'created_at', ]
