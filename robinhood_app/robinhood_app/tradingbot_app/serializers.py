
from rest_framework.serializers import ModelSerializer
from robinhood_app.robinhood_app.tradingbot_app.models import AboutInfo_Crypto


class AboutInfo_CryptoSerializer(ModelSerializer):
    
    class Meta:
        model = AboutInfo_Crypto
        fields = [
            'asset_currency',
            'display_only',
            'max_order_size',
            'min_order_size',
            'min_order_price_increment',
            'min_order_quantity_increment',
            'name',
            'quote_currency',
            'symbol',
            'tradability'
        ]
