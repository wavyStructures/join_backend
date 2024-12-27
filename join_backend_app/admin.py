from django.contrib import admin
from .models import User, Task, Contact, Board
# , BoardTask

# Register your models here.

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Contact)
admin.site.register(Board)
# admin.site.register(BoardTask)