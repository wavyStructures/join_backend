from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, default="123456789")
    color = models.CharField(max_length=100, null=True, blank=True)
    is_guest = models.BooleanField(default=False)
    # last_activity = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # def update_activity(self):
    #     self.last_activity = now()
    #     self.save(update_fields=['last_activity'])

    def save(self, *args, **kwargs):
        if self.username == "guest":
            self.set_unusable_password()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email