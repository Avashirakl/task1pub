from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Task, TaskChanging, Notification


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
        fields = ['id', 'name', 'description', 'author', 'status', 'previousstatus', 'start_date', 'end_date', 'spectators']


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'author', 'spectators', 'status', 'previousstatus', 'changed_by', 'end_date']
        read_only_fields = ['id', 'name', 'description', 'author', 'spectators']

    def update(self, instance, validated_data):
        tasks = validated_data.pop
        instance.previousstatus = instance.status
        varprev = instance.previousstatus
        instance.status = validated_data.get('status', instance.status)
        varstat = instance.status
        instance.save()
        return instance

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']


class TaskChangingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskChanging
        fields = ['id', 'task', 'currentstatus', 'prevstatus', 'changed_by', ]

    # def to_representation(self, instance):
    #     representation = super(TaskChangingSerializer, self).to_representation(instance)
    #     representation['status'] = TaskStatusSerializer(instance=instance.task).data
    #     return representation


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'previousstatus']


class NotificationSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'text', 'users', 'task', 'created_at', ]
