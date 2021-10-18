from django.shortcuts import render
from django.http import  JsonResponse


from robinhood_app.tradingbot_app.models import AboutInfo_Crypto


def index(request):
    return render(request, 'home.html', {'aboutInfo': aboutInfo})

def aboutInfo(request):  
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    # Check if Get Ajax Request
    if is_ajax:
        if request.method == 'GET': 
            aboutInfo = AboutInfo_Crypto.objects.all()
            return JsonResponse({'aboutInfo': list(aboutInfo.values())})

   


                
            