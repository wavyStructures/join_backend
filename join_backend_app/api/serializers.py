from rest_framework import serializers
from join_backend_app.models import Task, Contact


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# class BoardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Board
#         fields = '__all__'