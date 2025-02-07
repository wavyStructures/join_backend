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
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ManyToManyField(Contact, related_name='assigned_tasks')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='category-1')
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title
    
    