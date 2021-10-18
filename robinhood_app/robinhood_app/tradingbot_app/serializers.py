
from rest_framework.serializers import ModelSerializer
from .models import AboutInfo_Crypto


class AboutInfo_CryptoSerializer(ModelSerializer): 
    class Meta:
        model = AboutInfo_Crypto
        fields = ('__all__')