from django.http import HttpResponse
from django.shortcuts import render
import os, requests, json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data(request):
    return render(request, 'data.json')

def APItest(request):
    requestData = requests.get('http://api.vworld.kr/req/data?service=data&request=GetFeature&data=LT_C_UPISUQ151&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&attrFilter=emdCd:=:41465102')
    jsonData = None
    if requestData.status_code == 200:
        jsonData = requestData.json()
        f = open("./map/templates/data.json", 'w', encoding='utf-8')
        f.write(str(jsonData.get('response').get('result').get('featureCollection')).replace('\'', '"'))
        f.close()
        print(requestData.status_code, "Request OK")
    return HttpResponse(requestData)