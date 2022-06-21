from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def road(request):
    return render(request, 'road.html')

def land(request):
    return render(request, 'land.html')

def data(request):
    return render(request, 'data.json')

def landData(request):
    return render(request, 'landData.json')

def roadData(request):
    return render(request, 'roadData.json')


def API(request):
    yongin_emdcd = YongIn_regionName()
    featureCollection = {"type": "FeatureCollection",
                         "bbox": [127.00212289179542, 37.09498614424044, 127.45205299927372, 37.38706567868086],
                         "features": []}

    for emdcd in yongin_emdcd:
        url = "http://api.vworld.kr/req/data?service=data&request=GetFeature&data=LT_C_UPISUQ151&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&attrFilter=emdCd:=:"
        requestData = requests.get(url + emdcd)
        jsonData = None

        if requestData.status_code == 200:
            jsonData = requestData.json()
            # print(requestData.status_code, "Request OK")
            features = jsonData.get('response').get('result').get('featureCollection').get("features")
            for f in features:
                featureCollection.get("features").append(f)

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
        except:
            pass

    f = open("./map/templates/data.json", 'w', encoding='utf-8')
    f.write(str(featureCollection).replace('\'', '"'))
    f.close()

    return redirect('index')

def road_API(request):
    url = "http://api.vworld.kr/req/data?service=data&request=GetFeature&data=LT_C_UPISUQ151&key=5CC27E65-1081-3E65-A3F8-1EDD66DE7ECF&domain=http:127.0.0.1:8000&attrFilter=emdCd:=:"
    yongin_emdcd = YongIn_regionName()
    featureCollection = {"type": "FeatureCollection", "bbox": [127.00212289179542, 37.09498614424044, 127.45205299927372, 37.38706567868086], "features": []}

    for emdcd in yongin_emdcd:
        requestData = requests.get(url + emdcd)
        jsonData = None
        
        if requestData.status_code == 200:
            jsonData = requestData.json()
            # print(requestData.status_code, "Request OK")
            features = jsonData.get('response').get('result').get('featureCollection').get("features")
            for f in features:
                featureCollection.get("features").append(f)

    f = open("./map/templates/roadData.json", 'w', encoding='utf-8')
    f.write(str(featureCollection).replace('\'', '"'))
    f.close()

    print("yongin road info upload success")
    
    return redirect('road')


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
            # print(requestData.status_code, "Request OK - ", gu)

            jsonData = requestData.json()

            features = jsonData.get('response').get('result').get('featureCollection').get('features')

            for f in features:

                yongin_emdcd.append(f.get('properties').get('emd_cd'))

    return yongin_emdcd


def land_API(request):
    featureCollection = {"type": "FeatureCollection",
                         "bbox": [127.00212289179542, 37.09498614424044, 127.45205299927372, 37.38706567868086],
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
        except:
            pass
    f = open("./map/templates/landData.json", 'w', encoding='utf-8')
    f.write(str(featureCollection).replace('\'', '"'))
    f.close()

    return redirect('land')