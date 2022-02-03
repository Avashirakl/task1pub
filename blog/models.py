import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


STATUS_CHOICES = [
    ('P', "Planning"),
    ('A', "Active"),
    ('C', "Control"),
    ('D', "Done"),
    ]


class Task(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    name = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='author')
    spectators = models.ManyToManyField(User, related_name='spectator', null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='P')
    previousstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='changer')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class TaskChanging(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='stats', null=True)
    prevstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True, )
    currentstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True,)

    def __str__(self):
        return self.task.name


class TaskHistory(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    previousstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True)
    nextstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True)


class Notification(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    users = models.ManyToManyField(User, related_name='notifications', null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField(default="", null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
