from django.test import TestCase
from django.core.management import call_command
from django_dynamic_fixture import G
from django.test.client import Client


from robinhood_app.tradingbot_app.models import AboutInfo_Crypto

# Create your tests here.
class IndexCryptoAboutInfo(TestCase):
    """
    Tests for the process that retrieves and indexes starships from the SWAPI
    """
    def test_index_CryptoInfo(self):
         # Index Crypto
        call_command('index_CryptoInfo')

        # Check if there is more than one crypto
        self.assertGreater(AboutInfo_Crypto.objects.count(), 1)

class AjaxTest(TestCase):
    """
    Tests for 200 responses are returned for the Ajax Call. 
    """    
    def test_200_Responses(self):

        client = Client()
        with self.assertNumQueries(1):
            response = client.get("/aboutInfo-list", **{'HTTP_X_REQUESTED_WITH': 
        'XMLHttpRequest'})
            self.assertEqual(response.status_code, 200) 
        
