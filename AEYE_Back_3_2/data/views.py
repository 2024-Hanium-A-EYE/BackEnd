from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import DataModel
from .serializers import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serialzer = DataSerializer

    # GET 요청에 대한 로직 정의 (목록 조회)
    def list (self, request) :
        queryset = self.get_queryset()
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # POST 요청에 대한 로직 정의 (객체 생성)
    def create(self, request) :
        serializer = DataSerializer(data = request.data)
        if serializer.is_valid() :
            print("Valid Request!!")
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        print("Invalid Request!!")
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)