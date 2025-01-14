from django.urls import path
from .views import TaskListCreateView, TaskDetailView, ContactDetailView, ContactListCreateView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('contact/', ContactDetailView.as_view(), name='contact-detail'),
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
]