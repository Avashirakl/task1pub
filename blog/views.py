from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import TaskSerializer, UserSerializer, TaskChangingSerializer, NotificationSerialiazer
from .models import Task, TaskChanging, Notification
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


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

        email = EmailMessage('Notification about task', task, to=[user_email])
        email.send()
        return Response(status=200)

    