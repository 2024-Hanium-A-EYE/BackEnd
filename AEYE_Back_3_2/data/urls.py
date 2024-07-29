from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataViewSet

router = DefaultRouter()
router.register(r'front', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
