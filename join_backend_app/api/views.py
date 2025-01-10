from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from join_backend_app.models import  Task, Contact
from user_auth_app.models import UserProfile
from .serializers import TaskSerializer, ContactSerializer
# from .serializers import UserSerializer, TaskSerializer, ContactSerializer, BoardSerializer


    
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        # Fetch the UserProfile instance linked to the currently logged-in user
        user_profile = self.request.user.userprofile  # Access the related UserProfile
        serializer.save(user=user_profile)  # Save the UserProfile instance to the Contact
        
        

    
class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# class BoardViewSet(viewsets.ModelViewSet):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
    
    
