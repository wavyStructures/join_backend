from rest_framework import serializers
from user_auth_app.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone']  # Add fields specific to your custom user
        extra_kwargs = {'password': {'write_only': True}}  # Ensure passwords are write-only

    def create(self, validated_data):
        # Use `create_user` to handle password hashing
        return CustomUser.objects.create_user(**validated_data)