from django.shortcuts import render
from django.http import HttpResponse
from .models import weather_class
from .forms import Cities
import os
import requests
import json
def weather(city):
    url = "https://api.weatherbit.io/v2.0/current?city={}&key="
    API_KEY = os.environ["weather_api"]
    //Enter your api key above ....
    data = requests.get(url.format(city)+API_KEY)
    lis = json.loads(data.text)
    return {"icon":lis['data'][0]['weather']['icon'],"des":lis['data'][0]['weather']['description'],"date":lis['data'][0]['ob_time'],"city":lis['data'][0]['city_name'],"temp":lis['data'][0]['app_temp'],"clouds":lis['data'][0]['clouds'],"speed":lis['data'][0]['wind_spd'],"dir":lis['data'][0]['wind_cdir_full']}

def index(request):
    if(request.method == "POST"):
        Form = Cities(request.POST)
        if(Form.is_valid()):
            test = weather(request.POST["city"])
    else:
        Form = Cities()
        test = {}
    context = {"weather":test,"form":Form}
    return render(request, 'index.html',context)
