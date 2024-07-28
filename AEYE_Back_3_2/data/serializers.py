from rest_framework import serializers
from .models import DataModel

# Define JSON transfer

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'