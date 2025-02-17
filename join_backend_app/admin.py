from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_public')  
    list_filter = ('is_public',) 