from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/api/', include('user_auth_app.api.urls')),
    path('join/api/', include('join_backend_app.api.urls')),
]









# from .views import UserList, UserDetail, TaskList, TaskDetail, ContactList, ContactDetail, BoardViewSet

# urlpatterns = [
#     path('user-list/', UserList.as_view(), name='user-list'),
# ]