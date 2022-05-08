from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


def sendemail(user, task, description, status, deadline):
    email = EmailMessage('Notification about your task', "Task name: " +
                         task + '\n Task description: ' +
                         description + '\n Task status: '
                         + status + "\n Deadline:" +
                         deadline + "\n \n Please check your task.", to=[user])

    email.send()
    return HttpResponse('Success')


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerialiazer

    def create(self, request, *args, **kwargs):
        responce = super(NotificationViewSet, self).create(request, *args, **kwargs)
        # user = User.objects.get(id=request.data['users'])
        task = Task.objects.get(id=request.data['task'])
        tasks = request.data['task']
        deadline = task.end_date.strftime("%d-%b-%Y (%H:%M:%S)")
        sendemail(task.author.email, task.name, task.description, task.status, deadline)
        return responce
