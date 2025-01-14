from django.db import models
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

# Task model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status_choices = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

# Contact model
class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact', null=True)
    additional_info = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email if self.user else 'No User'}"