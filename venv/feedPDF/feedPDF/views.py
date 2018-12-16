from django.shortcuts import render
import pyrebase
import config


firebase = pyrebase.initialize_app(config)

