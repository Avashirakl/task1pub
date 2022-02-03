from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, TaskViewSet, TaskChangingViewSet, NotificationViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'taskchanging', TaskChangingViewSet, basename='taskch')
router.register(r'notifications', NotificationViewSet, basename='notification')


urlpatterns = [
    path('', include(router.urls)),
]
