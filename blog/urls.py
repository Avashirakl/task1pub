from django import urls
from django.urls import include, path
from .serializers import router
from . import views


urlpatterns = [
    path('', include(router.urls)),
    path('index', views.task_list, name='index'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('api-auth/', include('rest_framework.urls')),
]
