from django.urls import path
from user_auth_app.api.views import CustomUserListView, CustomUserDetailView, HelloView

urlpatterns = [
    path('users/', CustomUserListView.as_view(), name='user-list'),  
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),  
    path('hello/', HelloView.as_view(), name='hello'),
]

