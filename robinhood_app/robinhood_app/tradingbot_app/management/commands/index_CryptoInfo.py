from logging import getLogger
import requests
from django.core.management.base import BaseCommand
from robinhood_app.tradingbot_app.RBApi import RBApi
from robinhood_app.tradingbot_app.models import AboutInfo_Crypto
from manager_utils import upsert

LOG = getLogger(__name__)
'''
Takes External API Call From Crypto and Indexes to Data database

'''
class Command(BaseCommand):

    def handle(self, *args, **options):
        Rbapi = RBApi()
       
        for i in Rbapi._get_AboutInfo_Crypto():
            aboutInfoObj, created =  upsert(
                    AboutInfo_Crypto.objects,
                        name=i.get('name'),
                        symbol=i.get('symbol'),
                        tradability=i.get('tradability'),  
  
                      
                )
               




       


