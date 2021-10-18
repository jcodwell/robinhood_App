
from robinhood_app.tradingbot_app.models import AboutInfo_Crypto
from .serializers import AboutInfo_CryptoSerializer
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet
from rest_framework import renderers




class AboutInfo_CryptoModelViewSet(ModelViewSet):
    serializer_class = AboutInfo_CryptoSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.StaticHTMLRenderer)
    template_name = 'home.html'
    def get_queryset(self): 
        queryset = AboutInfo_Crypto.objects.all()
        return queryset
   
    
