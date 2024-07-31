from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Request_Data_ViewSet, Initate_AI_ViewSet
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'front', Request_Data_ViewSet)
router.register(r'initate-ai', Initate_AI_ViewSet)


urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

