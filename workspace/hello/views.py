from django.shortcuts import render
from django.http import HttpResponse
import time

def index(request):
    return HttpResponse("Hello, world! The time when you loaded this page was "+time.strftime("%c")+". At least somewhere.")
# Create your views here.
