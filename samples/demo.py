from MexcClient import MexcClient

import os
import time
from dotenv import load_dotenv

load_dotenv()
symbol = 'BTC_USDT'

client = MexcClient(api_key=os.getenv('U_ID'), is_testnet=True)

while True:
    opened_positions = client.get_open_positions()['data']
    if len(opened_positions) == 0:
        orders_data = client.get_open_orders({
            'symbol' : symbol,
            'is_finished' : 0,
        })['data']
        
        cs = client.create_order({
            'symbol': symbol,
            'type': 5, # Market
            'side': 3, # Open Short
            'openType': 1, # Isolated
            'vol': 1,
            'leverage': 200,
            'stopLossPrice': 110000,
            'takeProfitPrice': 90000,
        })

        cl = client.create_order({
            'symbol': symbol,
            'type': 5, # Market
            'side': 1, # Open Long
            'openType': 1, # Isolated
            'vol': 1,
            'leverage': 100,
            'stopLossPrice': 100000,
            'takeProfitPrice': 105000,
        })
        
        print(cs)
        print(cl)
        
    time.sleep(0.5)