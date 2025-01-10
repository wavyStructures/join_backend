
from rest_framework import generics
from rest_framework.decorators import api_view

from user_auth_app.models import UserProfile
from user_auth_app.api.serializers import UserProfileSerializer, RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken  

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            saved_account = serializer.save()
            
            token, created = Token.objects.get_or_create(user=saved_account)
                                
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
            }
           
        else:
            data = serializer.errors 
 
        return Response(data)
    

class CustomLoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

