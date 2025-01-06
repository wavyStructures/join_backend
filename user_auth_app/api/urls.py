from django.urls import path
from .views import UserProfileList, UserProfileDetail, RegistrationView, CustomLoginView
from rest_framework.authtoken.views import obtain_auth_token

# from user_auth_app.api.views import login_user


urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    # path('api/login/', login_user, name='login_user'),
]



from django.urls import path
from .views import UserRegistrationAPIView, LoginAPIView, UserProfileAPIView, UserProfileListAPIView, UserProfileDetailView

urlpatterns = [
    path('api/register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    
    path('api/profile/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('api/profiles/', UserProfileListAPIView.as_view(), name='user-profiles'),
]

