from rest_framework import serializers
from .models import getRequestModel

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = getRequestModel
        fields = '__all__'
