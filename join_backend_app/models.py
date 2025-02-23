from django.db import models
from django.contrib.auth import get_user_model
import random
import json

User = get_user_model()

def get_default_user():
    default_user = User.objects.get(email="guest@example.com")
    return default_user.id 

def generate_random_color():
    colors = [
        "#76b852", "#ff7043", "#ff3333", "#3399ff", "#ff6666",
        "#33ccff", "#ff9933", "#66ff66", "#0059ff", "#a64dff"
    ]
    return random.choice(colors)

# Contact model
class Contact(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True, unique=True)
    contactColor = models.CharField(max_length=7, blank=True, null=True)  
    contact_is_a_user = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts", default=get_default_user)

    def save(self, *args, **kwargs):
        if not self.contactColor:
            self.contactColor = generate_random_color()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Contact: {self.username if self.username else 'No Username'}"


# Task model
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    TYPE_CHOICES = [
        ('technical_task', 'Technical Task'),
        ('management_task', 'Management Task'),
        ('design_task', 'Design Task'),
        ('user_story', 'User Story'),
    ]

    CATEGORY_CHOICES = [
        ('category-0', 'Category 0'),
        ('category-1', 'Category 1'),
        ('category-2', 'Category 2'),
        ('category-3', 'Category 3'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ManyToManyField(Contact, related_name='assigned_tasks')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='category-1')
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    subtasks = models.JSONField(default=list)

    def __str__(self):
        return self.title
    
    