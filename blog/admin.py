from django.contrib import admin
from .models import Task, TaskChanging, Notification

admin.site.register(Task)
admin.site.register(TaskChanging)
admin.site.register(Notification)