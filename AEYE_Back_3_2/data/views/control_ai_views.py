from .views import *
from rest_framework import viewsets

from data.models import Initiate_AI_Model
from data.serializers import Initiate_AI_Serializer

# mehod 는 Test, Train, Inference 만 가능함.

# /api/data/ai-inference/ 
# ['method']
class Inference_AI_ViewSet(viewsets.ModelViewSet):
    pass

# /api/data/ai-test/
# ['method']
class Test_AI_ViewSet(viewsets.ModelViewSet):
    pass

# /api/data/ai-train/
# ['method']
class Train_AI_ViewSet(viewsets.ModelViewSet):
    pass
