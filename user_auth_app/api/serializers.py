from rest_framework import serializers
from user_auth_app.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  
        extra_kwargs = {'password': {'write_only': True}}  
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)