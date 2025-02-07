from rest_framework import serializers
from join_backend_app.models import Task, Contact
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)
           
    def validate_assigned_to(self, value):
        if not value:  # Check if value is empty
            raise serializers.ValidationError("Assigned contacts cannot be empty.")
        
        valid_contacts = Contact.objects.filter(id__in=[contact.id for contact in value])
        
        if len(valid_contacts) != len(value):
            raise serializers.ValidationError("One or more assigned contacts do not exist.")
        
        return value
        
        # users = Contact.objects.filter(id__in=[contact.id for contact in value])
        # if len(contacts) != len(value):
        #     raise serializers.ValidationError("One or more assigned contacts are not valid users.")
        # return contacts  

    class Meta:
        model = Task
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

