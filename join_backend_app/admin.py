from django.contrib import admin
from .models import  Task, Contact
from user_auth_app.models import UserProfile

# Register your models here.

# admin.site.register(User)
admin.site.register(Task)
admin.site.register(Contact)
# admin.site.register(Board)
admin.site.register(UserProfile)