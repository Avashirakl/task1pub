from django.contrib import admin

from blog.models import TaskChanging
from blog.models.task import Task
from blog.models.notifications import Notification


admin.site.register(Task)
admin.site.register(TaskChanging)
admin.site.register(Notification)