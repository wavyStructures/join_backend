from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TaskViewSet, ContactViewSet, BoardViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
