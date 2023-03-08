from MexcClient import MexcClient

import os
from dotenv import load_dotenv

import time
import math

load_dotenv()

symbol = 'BTC_USDT'

def main():
    client = MexcClient(api_key=os.getenv('U_ID'), is_testnet=True)
    try:
        client.cancel_all_trigger_orders({})
        
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
                    'leverage': 20,
                    #'stopLossPrice': 80,
                    #'takeProfitPrice': 80,
                })

                cl = client.create_order({
                    'symbol': 'BTC_USDT',
                    'type': 5, # Market
                    'side': 1, # Open Long
                    'openType': 1, # Isolated
                    'vol': 1,
                    'leverage': 20,
                    #'stopLossPrice': 80,
                    #'takeProfitPrice': 80,
                })
                
                print(cs)
                print(cl)
                
            time.sleep(0.5)
    finally:
        client.cancel_all_trigger_orders({})
        client.close_all_positions()

if __name__ == "__main__":
    main()