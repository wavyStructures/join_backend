from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
import random

def generate_random_color():
    colors = [
        "#76b852", "#ff7043", "#ff3333", "#3399ff", "#ff6666",
        "#33ccff", "#ff9933", "#66ff66", "#0059ff", "#a64dff"
    ]
    return random.choice(colors)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, default="123456789")
    contactColor = models.CharField(max_length=100, null=True, blank=True)
    
    is_guest = models.BooleanField(default=False)
    # last_activity = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    # objects = CustomUserManager()

    # def update_activity(self):
    #     self.last_activity = now()
    #     self.save(update_fields=['last_activity'])

    def save(self, *args, **kwargs):
        if self.username == "guest":
            self.set_unusable_password()
        if not self.contactColor:  
            self.contactColor = generate_random_color()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
