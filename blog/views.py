from django.utils import timezone
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'blog/index.html', {'tasks': tasks})