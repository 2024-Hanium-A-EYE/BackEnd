from .views import *
from rest_framework import viewsets

from data.models import Initiate_AI_Model
from data.serializers import Initiate_AI_Serializer

# /api/data/ai-inference/ Receive ['Image']
class Initate_AI_ViewSet(viewsets.ModelViewSet):
    queryset = Initiate_AI_Model.objects.all()
    serializer = Initiate_AI_Serializer

    def create(self, request) :
        log.print_log("SUCCESS", "Received Data From Client")
        serializer = Initiate_AI_Serializer(data = request.data)

        if serializer.is_valid() :
            
            log.print_log("SUCCESS", "Initiate AI", '[Initiate]')


            if(request.data == 'train'):
                files = {'name = train'}
                response = requests.post(ip.AI_Server_Address_Test, files=files)

                if (response == 200) :
                    log.print_log("SUCCESS", "Initiate AI Train")
                    return Response()
                else :
                    log.print_log("ERROR", "Failed to Initiate AI Train")
                    return Response()

            elif(request.data == 'test'):
                files = {'name = train'}
                reponse = requests.post(ip.AI_Server_Address_Test, files=files)

                if (reponse == 200) :
                    log.print_log("SUCCESS", "Initiate AI Test")
                    return Response()
                else:
                    log.print_log("ERROR", "Failed to Initiate AI Test")
                    return Response()

            return Response({"ERROR", 'Failed to Initiate AI'}, status = status.HTTP_200_OK)
        else :
            return Response({"ERROR", 'Server Received Wrong Valid Data!'}, status = status.HTTP_400_BAD_REQUEST)