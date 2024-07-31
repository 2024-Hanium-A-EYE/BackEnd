from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Request_Data_Model, Initiate_AI_Model
from .serializers import Request_Data_Serializer, Initiate_AI_Serializer
import requests
from colorama import Fore, Back, Style

AI_Server_Address_Inference = 'http://127.0.0.1:8000/api/ai-inference'
AI_Server_Address_Test = 'http://127.0.0.1:8000/api/'

SUCCESS = Fore.GREEN + "WEB - [SUCCESS]" + Fore.RESET
ERROR = Fore.RED + "WEB - [SUCCESS]" + Fore.RESET

def send_image_to_ai_server(image_path, server_url):
    with open(image_path, 'rb') as image_file:
        files = {'file' : image_file}
        reponse = requests.post(server_url, files=files)
        return reponse 


class Request_Data_ViewSet(viewsets.ModelViewSet):
    queryset = Request_Data_Model.objects.all()
    serializer = Request_Data_Serializer

    def create(self, request) :
        print(SUCCESS, "Received Data From Client")
        serializer = Request_Data_Serializer(data = request.data)

        if serializer.is_valid() :
    
            print(SUCCESS, "AI Inference Mode")
    
            oct_image = request.FILES['image']
            image_path = f'/tmp/{oct_image.name}'

            with open(image_path, 'wb+') as destination:
                for chunk in oct_image.chunks():
                    destination.write(chunk)
            print(SUCCESS, "Saved Image Data to Local Disk")


            response = send_image_to_ai_server(image_path, AI_Server_Address_Inference)

            if response.status_code == 200 :

                print(SUCCESS, "Send Data To AI")
                
                ## DataBase에 데이터 저장

                print(SUCCESS, "Saved Data to DataBase")

                ## DataBase에서 데이터 받음
                
                print(SUCCESS, "Received Data From DataBase")

                return Response({'[SUCCESS] AI Server Reciedved Correctly!'}, status=status.HTTP_201_CREATED)
            else :
                return Response('[ERROR] AI Server Received Wrong Data!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else :
            return Response('[ERROR] AI Server is Not Working!', status = status.HTTP_400_BAD_REQUEST)
    

class Initate_AI_ViewSet(viewsets.ModelViewSet):
    queryset = Initiate_AI_Model.objects.all()
    serializer = Initiate_AI_Serializer

    def create(self, request) :
        print(SUCCESS, "Received Data From Client")
        serializer = Initiate_AI_Serializer(data = request.data)

        if serializer.is_valid() :
            
            print(SUCCESS, "Initiate AI")


            if(request.data == 'train'):
                files = {'name = train'}
                response = requests.post(AI_Server_Address_Test, files=files)

                if (response == 200) :
                    print(SUCCESS, "Initiate AI Train")
                    return Response()
                else :
                    print(ERROR, "Failed to Initiate AI Train")
                    return Response()

            elif(request.data == 'test'):
                files = {'name = train'}
                reponse = requests.post(AI_Server_Address_Test, files=files)

                if (reponse == 200) :
                    print(SUCCESS, "Initiate AI Test")
                    return Response()
                else:
                    print(ERROR, "Failed to Initiate AI Test")
                    return Response()

            return Response({ERROR, 'Failed to Initiate AI'}, status = status.HTTP_200_OK)
        else :
            return Response({ERROR, 'Server Received Wrong Valid Data!'}, status = status.HTTP_400_BAD_REQUEST)