import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from blog.models.task import Task


class Notification(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    # users = models.ManyToManyField(User, related_name='notifications')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task.name