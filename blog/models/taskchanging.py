import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS_CHOICES = [
    ('P', "Planning"),
    ('A', "Active"),
    ('C', "Control"),
    ('D', "Done"),
    ]


class TaskChanging(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='stats', null=True)
    prevstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True, )
    currentstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True,)
    changed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task.name + " " + self.prevstatus + "-->" + self.currentstatus