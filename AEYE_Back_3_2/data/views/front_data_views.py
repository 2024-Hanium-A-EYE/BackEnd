from .views import *
from rest_framework import viewsets

from data.serializers import Front_Data_Serializer
from data.models import Front_Data_Model
    


# /api/data/front/ 
# Receive ['name', 'date', 'Image']
# Front -> Back -> AI
class Front_Data_ViewSet(viewsets.ModelViewSet):
    queryset = Front_Data_Model.objects.all().order_by('id')
    serializer_class = Front_Data_Serializer

    def create(self, request) :
        log.print_log("SUCCESS", "Received Data From Front", '[FRONT]')
        log.print_log_data(request.data)
        serializer = Front_Data_Serializer(data = request.data)

        if serializer.is_valid() :
            log.print_log("SUCCESS", "Received Valid Data", '[FRONT]')
            
            # Back -> AI
            url = ""
            response = send_image_to_ai(ip.ip.AI_Server_Address_Inference, request)

            return response
            
        else :
            return Response('["ERROR"] AI Server is Not Working!', status = status.HTTP_400_BAD_REQUEST)
    

def send_image_to_ai(server_url, request) :
    log.print_log("WORKING", "Saveing Image to Local Disk...", '[FRONT]')

    oct_image = request.FILES['image']
    image_path = f'/tmp/{oct_image.name}'

    with open(image_path, 'wb+') as destination:
        for chunk in oct_image.chunks():
                destination.write(chunk)
    
    log.print_log("SUCCESS", "Saved Image Data to Local Disk", '[FRONT]')

    # AI Server로 전송 #
    with open(image_path, 'rb') as image_file:
        files = {'file' : image_file}
        response = requests.post(server_url, files=files) 
    
    ###################
            
    if response.status_code == 200 :

        log.print_log("SUCCESS", "Send Data To AI", '[FRONT]')
        data = ""
        save_data_to_dataBase(data, '[FRONT]')
        data = get_data_from_dataBase('[FRONT]')
                
        log.print_log("SUCCESS", "Received Data From DataBase", '[FRONT]')

        return Response({'["SUCCESS"] AI Server Reciedved Correctly!'}, status=status.HTTP_201_CREATED)
    else :
        return Response('["ERROR"] AI Server Received Wrong Data!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


##################################################################################
# DataBase

# 여기에 pass 지우고 작성하면 됩니다. 
def save_data_to_dataBase(data, method) :
   log.print_log("WORKING", "Save Data to DataBase...", method)

   pass


def get_data_from_dataBase(method) :
    log.print_log("SUCCESS", "Saved Data to DataBase", method)

    pass