
from robinhood_app.robinhood_app.tradingbot_app.serializers import AboutInfo_CryptoSerializer
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet


class EncountersModelViewSet(ModelViewSet):
    def get_queryset(self):
        params = self.request.query_params
        key = params.get('show_id', 'ALL')  
        queryset = cache.get(key)
        if queryset is None:
         cache.set(key, self.queryset)
        return queryset or self.queryset
    serializer_class = AboutInfo_CryptoSerializer
