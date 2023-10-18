from django.shortcuts import render
import json
import urllib.request
def index (request):
    if request.method == 'POST' :
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid="use your own api here"').read()
        list_of_data=json.loads(source)            ##json.loads for objects,json.load(open()) for url(links)                                                    #######
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
    else:
        data={}
    return render(request,'main/index.html',data)      
# Create your views here.
