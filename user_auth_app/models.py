from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
import random

def generate_random_color():
    colors = [
        "#76b852", "#ff7043", "#ff3333", "#3399ff", "#ff6666",
        "#33ccff", "#ff9933", "#66ff66", "#0059ff", "#a64dff"
    ]
    return random.choice(colors)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, phone="123456789", **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)  # Hash the password!
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, phone="123456789", **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, phone, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[RegexValidator(
            regex=r"^[\w.@+\- ]+$",  # Allows spaces
            message="Enter a valid username. Only letters, numbers, spaces, and @/./+/-/_ are allowed.",
            code="invalid"
        )]
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, default="123456789")
    contactColor = models.CharField(max_length=100, null=True, blank=True)
    
    is_guest = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()  # ✅ Assign the custom manager here

    def save(self, *args, **kwargs):
        if self.username == "guest":
            self.set_unusable_password()
        if not self.contactColor:  
            self.contactColor = generate_random_color()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.timezone import now
# from django.core.validators import RegexValidator
# import random
# from django.contrib.auth.models import BaseUserManager



# def generate_random_color():
#     colors = [
#         "#76b852", "#ff7043", "#ff3333", "#3399ff", "#ff6666",
#         "#33ccff", "#ff9933", "#66ff66", "#0059ff", "#a64dff"
#     ]
#     return random.choice(colors)

# class CustomUser(AbstractUser):
#     username = models.CharField(
#         max_length=150,
#         unique=True,
#         validators=[RegexValidator(
#             regex=r"^[\w.@+\- ]+$",  # Allows spaces
#             message="Enter a valid username. Only letters, numbers, spaces, and @/./+/-/_ are allowed.",
#             code="invalid"
#         )]
#     )
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=20, default="123456789")
#     contactColor = models.CharField(max_length=100, null=True, blank=True)
    
#     is_guest = models.BooleanField(default=False)
#     # last_activity = models.DateTimeField(null=True, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
   
    
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None, phone="123456789", **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username, phone=phone, **extra_fields)
#         user.set_password(password)  # Hash the password!
#         user.save(using=self._db)
#         return user
    
#     objects = CustomUserManager()

#     # def update_activity(self):
#     #     self.last_activity = now()
#     #     self.save(update_fields=['last_activity'])

#     def save(self, *args, **kwargs):
#         if self.username == "guest":
#             self.set_unusable_password()
#         if not self.contactColor:  
#             self.contactColor = generate_random_color()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.email
    
