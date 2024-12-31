from rest_framework import generics
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer, RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken  

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

class CustomLoginView(ObteinAuthToken):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user'] q
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
            }
        else:
            data = serializer.errors 
 
        return Response(data)
  