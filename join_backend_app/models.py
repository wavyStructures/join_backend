from django.db import models
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

def get_default_user():
    default_user = User.objects.get(email="guest@example.com")
    return default_user.id 

# Contact model
class Contact(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    # additional_info = models.CharField(max_length=255, blank=True, null=True)
    contactColor = models.CharField(max_length=7, blank=True, null=True)  
    contact_is_a_user = models.BooleanField(default=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts", default=get_default_user)

    def __str__(self):
        return f"Contact: {self.username if self.username else 'No Username'}"



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