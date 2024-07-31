from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import DataModel
from .serializers import DataSerializer
import requests

class DataViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer = DataSerializer

    def create(self, request) :
        serializer = DataSerializer(data = request.data)
        
        if serializer.is_valid() :
            log.print("Valid Request!!")

            ## 데이터베이스 정의 ##
            serializer.save()
            
            ####################
            
            return Response(status = status.HTTP_200_OK)
        
        log.print("Invalid Request!!")
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    