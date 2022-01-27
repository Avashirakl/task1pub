from email.policy import default
from pydoc import describe
from pyexpat import model
import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title


class Task(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    taskname = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # spectators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    STATUS_CHOICES = [
    ('P', "Planning"),
    ('A', "Active"),
    ('C', "Control"),
    ('D', "Done"),
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='P')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.start_date = timezone.now()
        self.save()

    def __str__(self):
        return self.taskname

