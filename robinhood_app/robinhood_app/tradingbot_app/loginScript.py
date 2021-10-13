import robin_stocks as rs

"""rs.login(username=your_username,
         password=your_password,
         expiresIn=86400,
         by_sms=True)
"""
print(rs.robinhood.get_crypto_info('BTC'))         