from rest_framework import serializers
from join_backend_app.models import Task, Contact
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)
           
    def validate_assigned_to(self, value):
        if value:  
            valid_contacts = Contact.objects.filter(id__in=[contact.id for contact in value])
            if len(valid_contacts) != len(value):
                raise serializers.ValidationError("One or more assigned contacts do not exist.")
    
        return value
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user

        # assigned_contacts = validated_data.pop('assigned_to', [])
        assigned_contacts = validated_data.get('assigned_to', [])
        
        owner_contact = Contact.objects.filter(email=request.user.email).first()
        if owner_contact and owner_contact not in assigned_contacts:
            assigned_contacts.append(owner_contact)

        return super().create(validated_data)
        
    class Meta:
        model = Task
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


