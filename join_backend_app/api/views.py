from rest_framework import generics, permissions
from .permissions import IsAuthenticatedOrGuest  
from rest_framework.permissions import IsAuthenticated

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from join_backend_app.models import Task, Contact
from .serializers import TaskSerializer, ContactSerializer
from user_auth_app.api.serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
# from django.http import Http404
# from django.db.models import Q


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
        assigned_to = self.request.data.get('assigned_to', [])  
    
        # valid_contacts = Contact.objects.filter(id__in=assigned_to)
        
        # if len(valid_contacts) != len(assigned_to):
        #     raise ValidationError("Invalid contacts assigned.")

        # task = serializer.save(owner=self.request.user)
        # task.assigned_to.set(valid_contacts) 
         # Check if assigned_to is not empty or None
        if not assigned_to:
            # If empty, you could either set it to None, or leave it empty
            serializer.validated_data['assigned_to'] = []
            self.stdout.write(self.style.SUCCESS('No contacts assigned, leaving empty.'))

        else:
            # Validate that the contacts exist in the database
            valid_contacts = Contact.objects.filter(id__in=assigned_to)
            if len(valid_contacts) != len(assigned_to):
                raise ValidationError("Invalid contacts assigned.")

            # Set the valid contacts to the task
            serializer.validated_data['assigned_to'] = valid_contacts

        # Save the task with assigned contacts
        task = serializer.save(owner=self.request.user)

        # Only set the valid contacts if assigned_to was provided correctly
        if assigned_to:
            task.assigned_to.set(valid_contacts)
        else:
            task.assigned_to.clear()  # Optionally, clear if no contacts are assigned

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



