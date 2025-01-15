from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from user_auth_app.models import CustomUser
from user_auth_app.api.serializers import CustomUserSerializer

# List all users
class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.get_object()  

        if user != request.user:
            return Response({"detail": "You are not authorized to view this user's details."}, status=403)
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

# class SignUpView()