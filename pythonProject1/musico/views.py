from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    asd= loader.get_template('index.html')
    return HttpResponse(asd.render())