from rest_framework import serializers
from .models import Front_Data_Model, Initiate_AI_Model, Develop_Data_Model, Control_AI_Model

# Define JSON transfer

class Front_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Front_Data_Model
        fields = ['name', 'date', 'image']

class Control_AI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Control_AI_Model
        fields = ['method']

class Initiate_AI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Initiate_AI_Model
        fields = ['name']

class Develop_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Develop_Data_Model
        fields = ['name', 'date', 'image']