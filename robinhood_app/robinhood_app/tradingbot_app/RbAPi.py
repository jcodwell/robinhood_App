import robin_stocks as rs
from manager_utils import upsert
from models import AboutInfo_Crypto

print(rs.robinhood.get_crypto_info('BTC'))     

class Command(BaseCommand):
    
    def handle(self, *args, **options):


      def __init__(self) -> None:
          self.symbol = ''
          self.cryptoInfo = ''
          
    
    
      def getCryptoInfo(self, symbol):
          print(rs.robinhood.get_crypto_info(self.symbol))
          self.cryptoInfo = rs.robinhood.get_crypto_info(self.symbol)
          cryptoInfoObj, created = upsert(
                      AboutInfo_Crypto.objects,
                      asset_currency=self.cryptoInfo.get('asset_currency'),
                      display_only=self.cryptoInfo.get('display_only'),
                      max_order_size=self.cryptoInfo.get('max_order_size'), 
                      min_order_size=self.cryptoInfo.get('min_order_size'),
                      min_order_price_increment=self.cryptoInfo.get('min_order_price_increment'),
                      min_order_quantity_increment=self.cryptoInfo.get('min_order_quantity_increment'), 
                      name=self.cryptoInfo.get('name'),
                      quote_currency=self.cryptoInfo.get('quote_currency'),
                      symbol=self.cryptoInfo.get('symbol'),
                      tradability=self.cryptoInfo.get('tradability'), 
                  )
    

