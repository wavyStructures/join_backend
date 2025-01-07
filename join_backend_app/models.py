from django.db import models
from user_auth_app.models import UserProfile

# Create your models here.
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    users_assigned_to = models.ManyToManyField(UserProfile)    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default="2")  
    category = models.CharField(max_length=255, default="general")  
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Board(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
    
# # Optional: Linking tasks to boards
# # class BoardTask(models.Model):
# #     board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
# #     task = models.ForeignKey(Task, on_delete=models.CASCADE)

