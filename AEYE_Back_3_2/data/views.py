from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import DataModel
from .serializers import DataSerializer
import requests
from django.http import JsonResponse


AI_Server_Address = 'http://127.0.0.1:8000/api/receive-image'

def send_image_to_ai_server(image_path, server_url):
    with open(image_path, 'rb') as image_file:
        files = {'file' : image_file}
        reponse = requests.post(server_url, files=files)
        return reponse 


class DataViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer = DataSerializer

    def create(self, request) :
        serializer = DataSerializer(data = request.data)
        
        if serializer.is_valid() :


            print("===============Received Data From Client===============")
            oct_image = request.FILES['image']
            image_path = f'/tmp/{oct_image.name}'

            with open(image_path, 'wb+') as destination:
                for chunk in oct_image.chunks():
                    destination.write(chunk)
            print("===============Saved Image Data to Local Disk===============")


            response = send_image_to_ai_server(image_path, AI_Server_Address)
            print("===============Send Data To AI===============")


            if response.status_code == 200 :

                print("===============Received Data From AI===============")
                
                ## DataBase에 데이터 저장

                print("===============Saved Data to DataBase===============")

                ## DataBase에서 데이터 받음
                
                print("===============Received Data From DataBase===============")

                return Response('AI Server Reciedved Correctly!', status=status.HTTP_201_CREATED)
            else :
                return Response('AI Server Received Wrong Data!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else :
            return Response('AI Server is Not Working!', status = status.HTTP_400_BAD_REQUEST)
    
    