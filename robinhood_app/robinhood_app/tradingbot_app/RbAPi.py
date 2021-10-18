import requests



class RBApi(object):
    """
    An interface to the Robin Hood Crypto API Returns the ABout info for crypto
    """
    def __init__(self):
        self._initialize()

    def _initialize(self):
        self.aboutInfo_url = 'https://nummus.robinhood.com/currency_pairs/'

    def _get_AboutInfo_Crypto(self):
        """
        Robin Hood does not support a lot of crypto so pagination is not necessary. 
        Return the results.
        """
        # Get the results 
        response = requests.get(self.aboutInfo_url).json()
        return response.get('results')
