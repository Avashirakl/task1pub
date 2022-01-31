
from telnetlib import STATUS
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid



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

STATUS_CHOICES = [
    ('Planning', "Planning"),
    ('Active', "Active"),
    ('Control', "Control"),
    ('Done', "Done"),
    ]

class Task(models.Model):
    # id = models.UUIDField(
    #      primary_key = True,
    #      default = uuid.uuid4,
    #      editable = False) 
    name = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    spectators = models.ManyToManyField(User)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Planning')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.start_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



class TaskChanging(models.Model):
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    prevstatus = models.CharField(max_length=9, choices=STATUS_CHOICES)
    currentstatus = Task.status

    def __str__(self):
        return self.currentstatus


class Notification(models.Model):
    users = models.ManyToManyField(User.objects.get('email'))
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    notification_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task
