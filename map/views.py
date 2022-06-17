from django.http import HttpResponse
from django.shortcuts import render
import os, requests, json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data(request):
    return render(request, 'data.json')

def APItest(request):
    requestData = requests.get('http://api.vworld.kr/req/data?key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&service=data&version=2.0&request=getfeature&format=json&size=10&page=1&data=LT_C_ADSIDO_INFO&attrfilter=ctprvn_cd:=:41&columns=ctprvn_cd,ctp_kor_nm,ctp_eng_nm,ag_geom&geometry=true&attribute=true')
    jsonData = None
    if requestData.status_code == 200:
        jsonData = requestData.json()
        f = open("./map/templates/data.json", 'w')
        f.write(str(jsonData.get('response').get('result').get('featureCollection')))
        f.close()
        print(requestData.status_code, "Request OK")
    return HttpResponse(requestData)