from .views import *
from rest_framework import viewsets

from data.models import Develop_Data_Model
from data.serializers import Develop_Data_Serializer

# /api/data/developing/
# ['name', 'date', 'image']
class Developing_ViewSet(viewsets.ModelViewSet):
    queryset = Develop_Data_Model.objects.all().order_by('id')
    serializer_class = Develop_Data_Serializer

    def create(self, request) :
        log.print_log("SUCCESS", "Received Data From Front", '[DEVELOP]')
        log.print_log_data(request.data)
        serializer = Develop_Data_Serializer(data = request.data)

        if serializer.is_valid() :
            log.print_log("SUCCESS", "Received Valid Data", '[DEVELOP]')
            
            # Back -> AI
            response = send_image_to_ai(ip.AI_Server_Address_Inference, request)
            
            return response
            
        else :
            return Response('["ERROR"] AI Server is Not Working!', status = status.HTTP_400_BAD_REQUEST)
    

def send_image_to_ai(server_url, request) :
    log.print_log("WORKING", "Saveing Image to Local Disk...", '[DEVELOP]')

    oct_image = request.FILES['image']
    image_path = f'/tmp/{oct_image.name}'

    with open(image_path, 'wb+') as destination:
        for chunk in oct_image.chunks():
                destination.write(chunk)
    
    log.print_log("SUCCESS", "Saved Image Data to Local Disk", '[DEVELOP]')

    # AI Server로 전송 #
    with open(image_path, 'rb') as image_file:
        files = {'file' : image_file}
        response = requests.post(server_url, files=files) 
    
    ###################
            
    if response.status_code == 200 :

        log.print_log("SUCCESS", "Send Data To AI", '[DEVELOP]')
        data = ""
        save_data_to_dataBase(data, '[DEVELOP]')
        data = get_data_from_dataBase('[DEVELOP]')
                
        log.print_log("SUCCESS", "Received Data From DataBase", '[FRONT]')

        return Response({'["SUCCESS"] AI Server Reciedved Correctly!'}, status=status.HTTP_201_CREATED)
    else :
        return Response('["ERROR"] AI Server Received Wrong Data!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##################################################################################
# DataBase

# 여기에 pass 지우고 작성하면 됩니다. 
def save_data_to_dataBase(data, method) :
   log.print_log("WORKING", "Save Data to Local Disk...", method)

   pass


def get_data_from_dataBase(method) :
    log.print_log("SUCCESS", "Saved Data to Local Disk", method)

    pass