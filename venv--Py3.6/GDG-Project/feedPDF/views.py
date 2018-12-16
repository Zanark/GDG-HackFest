from django.shortcuts import render
import pyrebase
from . import config


firebase = pyrebase.initialize_app(config.config)

def index(request):
    return render(request , "index.html")

def feedDATA(request):
    db = firebase.database()

    json = 'json value'

    data = {
        "test" : "value"
    } 

    db.child("samples").child("bills").set(data)
    
    return render(request , "data_feeded.html")
    




    