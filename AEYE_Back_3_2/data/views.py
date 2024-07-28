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

            # get image
            # image_file = Image path
            url = "AI Server API"
            
            # make JSON FILES
            files = {'image' : 'imagefile'}
            response = requests.post(url, files = files)

            if response.status_code == 201:
                data = response.json()
                return JsonResponse(data, safe = False, status = 201)
            else :
                return JsonResponse("error", status = response.status_code)
        
        print("Invalid Request!!")
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    