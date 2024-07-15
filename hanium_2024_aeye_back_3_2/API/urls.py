from django.urls import path, include
from .views import getRequest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', getRequest, basename = 'event')

urlpatterns = [
        path('', include(router.urls)),
]
