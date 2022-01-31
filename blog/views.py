from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from .forms import TaskForm
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from blog import serializers


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializers = TaskSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,)) 
def apiOverview(request):
    api_urls = {
        'Task List' : '/tasklist/',
        'Task Detail' : '/taskdetail/<str:pk>/',
        'Task New' : '/tasknew/',
        'Task Edit' : '/taskedit/<str:pk>',
        'Delete' : '/taskdelete/<str:pk>',
    }
    
    return Response(api_urls)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,)) 
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,)) 
def taskdetail(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,)) 
def tasknew(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,)) 
def taskedit(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance = task, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,)) 
def taskdelete(pk):
    task = Task.objects.get(id = pk)
    task.delete()

    return Response('Deleted')






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
