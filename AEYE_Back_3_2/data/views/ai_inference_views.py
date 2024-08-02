from .views import *
from rest_framework import viewsets
from data.serializers import Request_Data_Serializer

def send_image_to_ai_server(image_path, server_url):
    with open(image_path, 'rb') as image_file:
        files = {'file' : image_file}
        reponse = requests.post(server_url, files=files)
        return reponse 


# /api/data/front/ Receive ['name', 'date', 'Image']
class Request_Data_ViewSet(viewsets.ModelViewSet):
    queryset = Request_Data_Model.objects.all().order_by('id')
    serializer_class = Request_Data_Serializer

    def create(self, request) :
        log.print_log("SUCCESS", "Received Data From Client")
        serializer = Request_Data_Serializer(data = request.data)

        if serializer.is_valid() :
    
            log.print_log("SUCCESS", "AI Inference Mode")
    
            oct_image = request.FILES['image']
            image_path = f'/tmp/{oct_image.name}'

            with open(image_path, 'wb+') as destination:
                for chunk in oct_image.chunks():
                    destination.write(chunk)
            log.print_log("SUCCESS", "Saved Image Data to Local Disk")

            # AI Server로 전송 #
            response = send_image_to_ai_server(image_path, ip.AI_Server_Address_Inference)
            ###################
            
            if response.status_code == 200 :

                log.print_log("SUCCESS", "Send Data To AI")
                
                ## DataBase에 데이터 저장

                log.print_log("SUCCESS", "Saved Data to DataBase")

                ## DataBase에서 데이터 받음
                
                log.print_log("SUCCESS", "Received Data From DataBase")

                return Response({'["SUCCESS"] AI Server Reciedved Correctly!'}, status=status.HTTP_201_CREATED)
            else :
                return Response('["ERROR"] AI Server Received Wrong Data!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else :
            return Response('["ERROR"] AI Server is Not Working!', status = status.HTTP_400_BAD_REQUEST)
    
