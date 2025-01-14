from rest_framework.generics import ListAPIView, RetrieveAPIView
from user_auth_app.models import CustomUser
from user_auth_app.api.serializers import CustomUserSerializer

# List all users
class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer