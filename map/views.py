from django.http import HttpResponse
from django.shortcuts import render
import os, requests, json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def road(request):
    return render(request, 'road.html')

def land(request):
    return render(request, 'land.html')

def landData(request):
    return render(request, 'landData.json')

def roadData(request):
    return render(request, 'roadData.json')

def road_API(request):

    requestData = requests.get('http://api.vworld.kr/req/data?service=data&request=GetFeature&data=LT_C_UPISUQ151&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&attrFilter=emdCd:=:41465102')

    jsonData = None
    if requestData.status_code == 200:
        jsonData = requestData.json()
        f = open("./map/templates/data.json", 'w', encoding='utf-8')
        f.write(str(jsonData.get('response').get('result').get('featureCollection')).replace('\'', '"'))
        f.close()
        print(requestData.status_code, "Request OK")
    return HttpResponse(requestData)

def YongIn_regionName():
    # 용인시 기흥구 : 41463
    # 용인시 수지구 : 41465
    # 용인시 처인구 : 41461

    url = "https://api.vworld.kr/req/data?key=CEB52025-E065-364C-9DBA-44880E3B02B8&domain=http://localhost:8080&service=data&version=2.0&request=getfeature&format=json&size=100&page=1&data=LT_C_ADEMD_INFO&geometry=true&attribute=true&attrfilter=emd_cd:like:"
    yongin_emdcd = []

    for gu in ["41463", "41465", "41461"]:
        requestData = requests.get(url + gu)
        jsonData = None

        if requestData.status_code == 200:
            print(requestData.status_code, "Request OK - ", gu)
            jsonData = requestData.json()

            features = jsonData.get('response').get('result').get('featureCollection').get('features')

            for f in features:
                # print(f.get('properties').get('full_nm'), f.get('properties').get('emd_cd'))
                yongin_emdcd.append(f.get('properties').get('emd_cd'))

    return yongin_emdcd


def land_API(request):
    # url = 'http://api.vworld.kr/req/data?service=data&request=GetFeature&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&data=LT_C_LHBLPN&attrFilter=emdCd:=:'
    # suzi = 41465101  # ~07
    # gihung = 41463101  # ~18
    # chuin = 41461250, 41461253, 41461256, 41461259, 41461340, 41461350, 41461360, 41461101, 41461102, 41461103, 41461104  # ~10
    featureCollection = {"type": "FeatureCollection",
                         "bbox": [127.10902550151559, 37.313950644559384, 127.13139439088252, 37.35114447412832],
                         "features": []}
    yongin_emdcd = YongIn_regionName()
    for i in yongin_emdcd:
        url = 'http://api.vworld.kr/req/data?service=data&request=GetFeature&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&data=LT_C_LHBLPN&attrFilter=emdCd:=:'
        url += str(i)
        try:
            requestData = requests.get(url)
            jsonData = None
            if requestData.status_code == 200:
                jsonData = requestData.json()
                features = jsonData.get('response').get('result').get('featureCollection').get("features")
                for f in features:
                    featureCollection.get("features").append(f)
                print(requestData.status_code, "Request OK")
                print(featureCollection)
        except:
            pass
    f = open("./map/templates/landData.json", 'w', encoding='utf-8')
    f.write(str(featureCollection).replace('\'', '"'))
    f.close()

    return HttpResponse(featureCollection)