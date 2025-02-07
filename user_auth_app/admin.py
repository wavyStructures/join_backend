from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add any fields you want to display in the admin list view
    list_display = ('email', 'username', 'phone', 'is_staff', 'is_superuser', 'is_guest', 'contactColor')
    list_filter = ('is_staff', 'is_superuser', 'is_guest')
    search_fields = ('email', 'username', 'phone')

    # Specify which fields can be edited directly in the list view
    ordering = ('email',)

    # Fields shown when editing a user in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'phone', 'contactColor', 'is_guest')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields shown when creating a new user in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'password1', 'password2'),
        }),
    )