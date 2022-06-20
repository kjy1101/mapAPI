from django.http import HttpResponse
from django.shortcuts import render
import os, requests, json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data(request):
    return render(request, 'data.json')


# 토지정보
def APItest(request):
    url = 'http://api.vworld.kr/req/data?service=data&request=GetFeature&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&data=LT_C_LHBLPN&attrFilter=emdCd:=:'
    suzi = 41465101 #~07
    gihung = 41463101 # ~18
    chuin = 41461250, 41461253, 41461256, 41461259, 41461340, 41461350, 41461360, 41461101, 41461102, 41461103, 41461104 # ~10
    requestData = requests.get('http://api.vworld.kr/req/data?service=data&request=GetFeature&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&data=LT_C_LHBLPN&attrFilter=emdCd:<=:41465101')
    jsonData = None
    if requestData.status_code == 200:
        jsonData = requestData.json()
        f = open("./map/templates/data.json", 'w', encoding='utf-8')
        f.write(str(jsonData.get('response').get('result').get('featureCollection')).replace('\'', '"'))
        f.close()
        print(requestData.status_code, "Request OK")
    return HttpResponse(requestData)