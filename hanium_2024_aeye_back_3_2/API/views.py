from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import getRequestModel
from .serializers import RequestSerializer

# Create your views here.

@api_view(['POST'])
def getRequest(request):
    if request.method == 'POST':
        serializer = RequestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # 여기서 Coding
    return HttpResponse("Hello! Connected Successfully!")

