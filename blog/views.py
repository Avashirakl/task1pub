from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from rest_framework.decorators import action

from .models import Notification
from .serializers import TaskListSerializer, TaskCreateSerializer, UserSerializer, TaskChangingSerializer, NotificationSerialiazer, TaskRetrieveSerializer, TaskUpdateSerializer
from blog.models.task import Task
from blog.models.taskchanging import TaskChanging
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
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


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerialiazer

    @action(methods=['POST'], detail=True, url_path='sendemail')
    def sendemail(self, request, *args, **kwargs):
        instance = self.get_object()
        user = User.objects.get(id=User.pk)
        user_email = user.email
        task = Task.objects.get(id=Task.pk)
        from_email = 'django2503@gmail.com'

        if user_email and task.name and from_email:
            try:
                send_mail(user.username, task.name, from_email, [user_email], auth_user='django250302@gmail.com', auth_password='adil250302')
            except BadHeaderError:
                return HttpResponse('Invalid.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    