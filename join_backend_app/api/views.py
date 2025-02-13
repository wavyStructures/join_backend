from rest_framework import generics, permissions
from .permissions import IsGuestOrReadOnly  
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from join_backend_app.models import Task, Contact
from .serializers import TaskSerializer, ContactSerializer
from user_auth_app.api.serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # Admins can see all tasks
            return Task.objects.all()

        user_contact = get_object_or_404(Contact, email=user.email)
        return Task.objects.filter(assigned_to=user_contact)
    
    def perform_create(self, serializer):
        assigned_to = self.request.data.get('assigned_to', [])  
    
        # valid_users = User.objects.filter(id__in=assigned_to)
        valid_contacts = Contact.objects.filter(id__in=assigned_to)
        
        # if len(valid_users) + len(valid_contacts) != len(assigned_to):
        if len(valid_contacts) != len(assigned_to):
            raise ValidationError("Invalid contacts assigned.")

        # serializer.save(owner=self.request.user, assigned_to=valid_contacts)
        task = serializer.save(owner=self.request.user)
        task.assigned_to.set(valid_contacts) 
        
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:  # Admins can see all tasks
            return Task.objects.all()
        
        user_contact = get_object_or_404(Contact, email=user.email)
        return Task.objects.filter(assigned_to=user_contact)

class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
          # Get the Contact instance for the logged-in user
        user_contact = get_object_or_404(Contact, email=self.request.user.email)
        
        # Return tasks where the user is one of the assigned contacts
        return Task.objects.filter(assigned_to=user_contact)
        # user = self.request.user.email
        # return Task.objects.filter(assigned_to=user)

  
    
    
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
         
#         try:
#             if request.user.is_superuser:
#                 tasks = Task.objects.all()
#             else:
#                 # Find the Contact instance linked to the logged-in user
#                 contact = Contact.objects.filter(user=request.user).first()
                
#                 if not contact:
#                     return Response({"error": "No contact found for this user."}, status=404)
                
#                 # Filter tasks where the contact is assigned OR the user is the owner
#                 tasks = Task.objects.filter(Q(assigned_to=contact) | Q(owner=request.user)).distinct()
            
#             serializer = TaskSerializer(tasks, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return Response({'error': str(e)}, status=500)
                 
# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsGuestOrReadOnly]  

    def get_queryset(self):
        return Contact.objects.all()

    def perform_create(self, serializer):
        if self.request.user.is_guest:
            raise PermissionDenied("Guests cannot create contacts.")
        serializer.save(user=self.request.user)


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsGuestOrReadOnly]

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

# Contact Views
# class ContactListCreateView(generics.ListCreateAPIView):
#     serializer_class = ContactSerializer

#     def get_queryset(self):
#         """
#         Return all contacts for the authenticated user.
#         """
#         return Contact.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         """
#         Handle creating a new contact. If it's a registered user, we automatically
#         consider them a contact.
#         If it's an unregistered contact, we save them with additional info.
#         """
#         contact_data = serializer.validated_data
#         user = contact_data.get('user')  # The user field (if exists)
#         additional_info = contact_data.get('additional_info')  # Extra info for unregistered contacts

#         # Case 1: If it's an unregistered user (with additional info)
#         if not user and additional_info:
#             serializer.save(user=self.request.user, additional_info=additional_info)

#         # Case 2: If it's a registered user, we don’t need to add them as contact manually because of the signal
#         elif user:
#             serializer.save(user=self.request.user)

#         else:
#             raise ValidationError("You must provide either a registered user or additional info.")