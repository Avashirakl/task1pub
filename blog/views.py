from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail 
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'blog/index.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'blog/task_detail.html', {'task': task})


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.start_date = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'blog/task_edit.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.start_date = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'blog/task_edit.html', {'form': form})
