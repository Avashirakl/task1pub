from django import urls
from django.urls import include, path
from . import views
from rest_framework import routers
from .views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.apiOverview, name = "api-overview"),
    path('tasklist/', views.tasklist, name = "tasklist"),
    path('tasknew/', views.tasknew, name = "tasknew"),
    path('taskdetail/', views.taskdetail, name = "taskdetail"),
    path('taskedit/', views.taskedit, name = "taskedit"),
    path('taskdelete/', views.taskdelete, name = "taskdelete"),
    path('api-auth/', include('rest_framework.urls')),



    path('index', views.task_list, name='index'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    
]
