import uuid
from django.db import models


STATUS_CHOICES = [
    ('P', "Planning"),
    ('A', "Active"),
    ('C', "Control"),
    ('D', "Done"),
    ]


class TaskHistory(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    previousstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True)
    nextstatus = models.CharField(max_length=9, choices=STATUS_CHOICES, null=True)