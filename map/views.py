from django.shortcuts import render
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data(request):
    return render(request, 'data.json')