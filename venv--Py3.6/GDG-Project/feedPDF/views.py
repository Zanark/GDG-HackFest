from django.shortcuts import render
import pyrebase
from . import config
from . import ocr
import subprocess

from django.shortcuts import render_to_response
from django.template import RequestContext

import random

firebase = pyrebase.initialize_app(config.config)

def index(request):
    return render(request , "index.html")

def feedDATA(request):
    db = firebase.database()

    # json = 'json value'

    # data = {
    #     "test" : "value"
    # } 
    #path = request.POST.get('pdf-name')
    path = "/home/zanark/CODING/GDG/HackFest/GDG-HackFest/venv--Py3.6/GDG-Project/static/pdf/OD114095206559588000.pdf"
    subprocess.call(["pdf2txt.py" , "-t" , "xml" , path , "-o" , "op.xml"])

    template_path = '/home/zanark/CODING/GDG/HackFest/GDG-HackFest/venv--Py3.6/GDG-Project/feedPDF/fk.yaml'
    xml_file = 'op.xml'

    data = ocr.get_json(template_path, xml_file)
    print(data)

    billname = "bill no."  +  str(random.randint(1, 1000000))

    db.child("samples").child("bill3").set(data)
    
    return render(request , "data_feeded.html")
    




    