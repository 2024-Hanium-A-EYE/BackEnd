from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.front_data_views import Front_Data_ViewSet
from .views.ai_setting_views import Initate_AI_ViewSet
from .views.developing_views import Developing_ViewSet
from .views.control_ai_views import Inference_AI_ViewSet, Train_AI_ViewSet, Test_AI_ViewSet

from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()

# Front API
router.register(r'front', Front_Data_ViewSet)
'''
['name', 'date', 'image']
'''


# Control API
router.register(r'ai', Initate_AI_ViewSet)

#router.register(r'ai-inference', Inference_AI_ViewSet)
#router.register(r'ai-test', Test_AI_ViewSet)
#router.register(r'ai-train', Train_AI_ViewSet)
'''
['method']
'''

# Developing API
router.register(r'developing', Developing_ViewSet)
'''
['name', 'date', 'image']
'''

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

