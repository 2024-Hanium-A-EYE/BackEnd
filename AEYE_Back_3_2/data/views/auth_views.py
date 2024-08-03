from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return HttpResponse("Logged out")