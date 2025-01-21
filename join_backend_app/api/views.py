from rest_framework import generics, permissions

from join_backend_app.models import Task, Contact
from .serializers import TaskSerializer, ContactSerializer
from user_auth_app.api.serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

from rest_framework.exceptions import ValidationError

User = get_user_model()

# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

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

class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        """
        Return contacts associated with the current authenticated user.
        """
        return Contact.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        """
        Add the contact and associate it with the current user.
        """
        contact = serializer.save()
        contact.users.add(self.request.user) 


class ContactDetailView(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    

