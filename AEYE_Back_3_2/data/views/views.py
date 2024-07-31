
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from data.models import Initiate_AI_Model, Request_Data_Model
import requests
import ip
import data.views.log as log
