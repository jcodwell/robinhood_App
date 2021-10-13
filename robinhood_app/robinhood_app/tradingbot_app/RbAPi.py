import robin_stocks as rs
from manager_utils import upsert

print(rs.robinhood.get_crypto_info('BTC'))     

class Intialize():


    def __init__(self) -> None:
        self.symbol = ''
        


    def getCryptoInfo(self, symbol):
        print(rs.robinhood.get_crypto_info(self.symbol))
                



