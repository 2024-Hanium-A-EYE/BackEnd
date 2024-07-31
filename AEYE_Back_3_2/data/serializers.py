from rest_framework import serializers
from .models import Request_Data_Model, Initiate_AI_Model

# Define JSON transfer

class Request_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Request_Data_Model
        fields = ['name', 'date', 'image']


class Initiate_AI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Initiate_AI_Model
        fields = ['name']