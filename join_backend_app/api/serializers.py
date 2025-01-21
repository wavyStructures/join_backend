from rest_framework import serializers
from join_backend_app.models import Task, Contact
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Task
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)  

    class Meta:
        model = Contact
        fields = ['id', 'users', 'additional_info', 'contactColor', 'username', 'phone']

    def validate(self, attrs):
        """
        Validate that at least one user or additional info is provided.
        """
        if not attrs.get('users') and not attrs.get('additional_info'):
            raise serializers.ValidationError("You must provide either associated users or additional info.")
        return attrs



