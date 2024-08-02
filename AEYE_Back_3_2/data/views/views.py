
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

import requests
import os, sys
from . import log

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.append(root_dir)

import ip