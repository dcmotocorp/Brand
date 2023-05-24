from rest_framework import serializers
from .models import Startups


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startups
        fields = "__all__" 
