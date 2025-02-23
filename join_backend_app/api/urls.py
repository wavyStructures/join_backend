from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserTasksView, ContactDetailView, ContactListCreateView, ContactListCreateView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/user/', UserTasksView.as_view(), name='user-tasks'),  

    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('user-contacts/', ContactListCreateView.as_view(), name='user-contacts'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]


