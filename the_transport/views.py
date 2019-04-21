from django.shortcuts import render,redirect
from django.conf import settings
from circuitbreaker import circuit
from logistics.models import Vehicle
from .models import Country
import requests,json, time, random

def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    assets_total=Vehicle.objects.count()
    assets_in_use=Vehicle.objects.filter(condition='WORKING').count()
    average_in_use=round((assets_in_use/assets_total)*100)
    average_not_in_use=100-average_in_use
    avg=[average_in_use,average_not_in_use]
    ctx={
        'avg':avg,
        'result':Vehicle.objects.all(),
        'time':dateManupulator()
    }

    return render(request,'index.html',ctx)
@circuit
def dateManupulator():
    url="http://api.timezonedb.com/v2.1/get-time-zone?key=TA24US0OU2V5&format=json&by=zone&zone={}"
    country_list=Country.objects.all()
    country_data_list=[]
    try:
        for country in country_list:
            ret=requests.get(url.format(country.zone)).json()
            country_data={
            'place':country.place,
            'time':ret['formatted']
            }
            country_data_list.append(country_data)
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        time.sleep(2**.01 + random.random()*0.01) #exponential backoff
        return dateManupulator()
    return country_data_list
