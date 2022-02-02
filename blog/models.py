from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from model_utils import FieldTracker

import uuid


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
    spectators = models.ManyToManyField(User, related_name='spectator')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='P')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    tracker = FieldTracker()
    prevstat = tracker.previous('status')

    def __str__(self):
        return self.name


class TaskChanging(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # prevstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True)

    @property
    def currentstatus(self):
        return self.task.status

    @property
    def prevstatus(self):
        return self.task.prevstat

    def __str__(self):
        return self.task.name


class Notification(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    users = models.ManyToManyField(User, related_name='notifications')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task.name
