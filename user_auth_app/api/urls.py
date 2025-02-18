from django.urls import path
from user_auth_app.api.views import CustomUserListCreateView, CustomUserDetailView, SignUpView, CheckEmailView, LoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', CustomUserListCreateView.as_view(), name='user-list'),  
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),  
    path('signup/', SignUpView.as_view(), name='signup'),
    path('auth-api/token/', obtain_auth_token, name='token_obtain'),
    path('check-email/', CheckEmailView.as_view(), name='check-email'), 
    path('login/', LoginView.as_view(), name='login'),
]

