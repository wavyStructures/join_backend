from django.contrib import admin
from django.urls import path, include
from .views import TaskList, TaskDetail, ContactList, ContactDetail
# , UserList, UserDetail, BoardViewSet


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('contacts/', ContactList.as_view(), name='contact-list'),  
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    # path('users/', UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    # path('boards/', BoardViewSet.as_view({'get': 'list', 'post': 'create'}), name='board-list'),
]











# from .views import UserList, UserDetail, TaskList, TaskDetail, ContactList, ContactDetail, BoardViewSet

# urlpatterns = [
#     path('user-list/', UserList.as_view(), name='user-list'),
# ]