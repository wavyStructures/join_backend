from rest_framework import generics, permissions
from .permissions import IsAuthenticatedOrGuest  
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from join_backend_app.models import Task, Contact
from .serializers import TaskSerializer, ContactSerializer
from user_auth_app.api.serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model


User = get_user_model()

# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrGuest]
    
    def get_queryset(self):
        print(self.request.headers)
        user = self.request.user
        
        if user.is_superuser:
            return Task.objects.all()
        
        if user.is_authenticated:
            user_contact = get_object_or_404(Contact, email=user.email)
            return Task.objects.filter(assigned_to=user_contact)
        
        elif user.email == 'guest@example.com':  
            guest_contact = get_object_or_404(Contact, id=84)
            return Task.objects.filter(assigned_to=guest_contact)

        return Task.objects.none()
    
    def perform_create(self, serializer):
        user = self.request.user
        assigned_to_ids = self.request.data.get('assigned_to', [])  
    
        valid_contacts = list(Contact.objects.filter(id__in=assigned_to_ids))
        
        owner_contact = Contact.objects.filter(email=user.email).first()
        if owner_contact and owner_contact not in valid_contacts:
            valid_contacts.append(owner_contact)
  
        task = serializer.save(owner=user)
        task.assigned_to.set(valid_contacts)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:  
            return Task.objects.all()
        
        user_contact = get_object_or_404(Contact, email=user.email)
        return Task.objects.filter(assigned_to=user_contact)

class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrGuest]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_contact = get_object_or_404(Contact, email=self.request.user.email)
        else:
            user_contact = get_object_or_404(Contact, id=84)
        
        return Task.objects.filter(assigned_to=user_contact)
       
                 
# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrGuest]  

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Contact.objects.all()
        return Contact.objects.filter(is_public=True)

    def perform_create(self, serializer):
        if self.request.user.is_guest:
            raise PermissionDenied("Guests cannot create contacts.")
        serializer.save(user=self.request.user)


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrGuest]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Contact.objects.all()
        return Contact.objects.filter(is_public=True)

    def perform_update(self, serializer):
        if self.request.user.is_guest:
            raise PermissionDenied("Guests cannot update contacts.")
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['delete'])
    def delete_contact(self, request, pk=None):
        contact = self.get_object()
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



