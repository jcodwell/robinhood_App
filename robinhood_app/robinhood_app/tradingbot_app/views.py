from django.shortcuts import render
from django.http import HttpResponse
import robin_stocks as rs
from django.http import HttpResponseBadRequest, JsonResponse


from robinhood_app.tradingbot_app.models import AboutInfo_Crypto


def index(request):
    return render(request, 'home.html', {'aboutInfo': aboutInfo})

def aboutInfo(request):   
        aboutInfo = AboutInfo_Crypto.objects.all()
        return JsonResponse({'aboutInfo': list(aboutInfo.values())})

   


                
            