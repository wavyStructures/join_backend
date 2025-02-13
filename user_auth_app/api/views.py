from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from user_auth_app.models import CustomUser
from user_auth_app.api.serializers import CustomUserSerializer, SignUpSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.get_object()  

        if not request.user.is_superuser and user != request.user:
            return Response({"detail": "You are not authorized to view this user's details."}, status=403)
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
class SignUpView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        # Only for testing purposes, to see a form in the browser
        return Response({
            "username": "",
            "email": "",
            "password": ""
        })

    def post(self, request, *args, **kwargs):
        try:
            serializer = SignUpSerializer(data=request.data)
            if serializer.is_valid():
                custom_user = serializer.save()
                token, created = Token.objects.get_or_create(user=custom_user)
                return Response({
                    "user": {
                        "username": custom_user.username,
                        "email": custom_user.email,
                        "password": custom_user.password,
                    },
                    "token": token.key,
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            import traceback
            print("🚨 Server Error:", str(e))
            print(traceback.format_exc())
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class SignUpView(APIView):
#     permission_classes = (AllowAny,)
    
#     def post(self, request, *args, **kwargs):
#         print("Request received with data:", request.data)
#         serializer = SignUpSerializer(data=request.data)
        
#         if serializer.is_valid():
#             custom_user = serializer.save()            
#             token, created = Token.objects.get_or_create(user=custom_user)
            
#             return Response({
#                  "user": {
#                     "username": custom_user.username,
#                     "email": custom_user.email,
#                     "phone": custom_user.phone,
#                 },
#                 "token": token.key,  
#             }, status=status.HTTP_201_CREATED)

#         print("Validation errors:", serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
       
class CheckEmailView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        exists = User.objects.filter(email=email).exists()
        return Response({'exists': exists})


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return Response({'error': 'Both email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
            },
            "token": token.key,  # Send the token to the frontend
        }, status=status.HTTP_200_OK)
        



class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)





