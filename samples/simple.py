from MexcClient import MexcClient

client = MexcClient(api_key='H507d7a8b2d3eac8f4bcbb561e815b27ad454d6ef91cd384169cf1a817ffe1b1dd', is_testnet=True)

orderShort = client.create_order({
    'symbol': 'BTC_USDT',
    'type': 5, # Market
    'side': 3, # Open Short
    'openType': 1, # Isolated
    'vol': 1,
    'leverage': 20,
    #'stopLossPrice': 80,
    #'takeProfitPrice': 80,
})
