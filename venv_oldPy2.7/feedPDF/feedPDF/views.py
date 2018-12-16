from django.shortcuts import render
import pyrebase
from . import config


firebase = pyrebase.initialize_app(config.config)

def feedDATA(request):
    return render(request , "index.html")


    