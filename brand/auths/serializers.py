# myapp/serializers.py

from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email', 'password', 'role','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}  # Password should not be included in response

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

