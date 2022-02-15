from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Notification
from .serializers import TaskListSerializer, TaskCreateSerializer, UserSerializer, TaskChangingSerializer, NotificationSerialiazer, TaskRetrieveSerializer, TaskUpdateSerializer
from blog.models.task import Task
from blog.models.taskchanging import TaskChanging


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskCreateSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == 'create':
            serializer = TaskCreateSerializer
        elif self.action == 'list':
            serializer = TaskListSerializer
        elif self.action == 'retrieve':
            serializer = TaskRetrieveSerializer
        elif self.action == 'update':
            serializer = TaskUpdateSerializer
        elif self.action == 'partial_update':
            serializer = TaskUpdateSerializer

        return serializer


class TaskChangingViewSet(viewsets.ModelViewSet):
    queryset = TaskChanging.objects.all()
    serializer_class = TaskChangingSerializer


def sendemail(user, tasks, task):
    email = EmailMessage('Notification about your task', "Your task id: " + tasks + " Task name: " + task, to=[user])
    email.send()
    return HttpResponse('Success')


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerialiazer

    def create(self, request, *args, **kwargs):
        responce = super(NotificationViewSet, self).create(request, *args, **kwargs)
        user = self.request.user.email
        task = Task.objects.get(id=request.data['task'])
        tasks = request.data['task']
        sendemail(user, tasks, task.name)
        return responce
