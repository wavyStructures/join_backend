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
    name = models.CharField(max_length=100, default="Max Mustermann")
    mail = models.CharField(max_length=100, default="Max@Musteremail.de")
    phone = models.CharField(max_length=100, default="012345678")
    # initials = models.CharField(max_length=5, default="MM")
    contactColor = models.CharField(max_length=20, default="#FF7A00")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='contacts')
    # user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='contacts')

    # created_at = models.DateTimeField(auto_now_add=True)
    
    #  def save(self, *args, **kwargs):
    #     # Automatically generate initials if not provided
    #     if not self.short:
    #         self.short = ''.join([part[0] for part in self.name.split()[:2]]).upper()
    #     super(ContactModel, self).save(*args, **kwargs)
   
    def __str__(self):
        return f'({self.id}) {self.name}'
    




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

