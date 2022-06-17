from django.shortcuts import render
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def geojson(request):
    return render(request, 'data.json')