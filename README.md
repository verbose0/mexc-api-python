<div align="center">
   <img src="https://github.com/verbose0/mexc-api-python/blob/main/assets/mexc_logo.jpg?raw=true" height="150" width="150">

  ![License: Proprietary](https://img.shields.io/badge/license-proprietary-red)
  ![Private Code](https://img.shields.io/badge/source-private-orange)
  ![Paid Access](https://img.shields.io/badge/access-paid-blue)
</div>


# 🔷 MEXC Futures API Python

This unofficial MEXC Futures API library circumvents the ongoing maintenance limitations of the official endpoints, enabling complete access to trading and account features—even when certain routes are marked as 'Under maintenance'

## 🚀 API initialization

```python
from MexcClient import MexcClient

client = MexcClient(api_key=os.getenv('YOUR_U_ID'), is_testnet=True)

orderShort = client.create_order({
    'symbol': 'BTC_USDT',
    'type': 5, # Market
    'side': 3, # Open Short
    'openType': 1, # Isolated
    'vol': 1,
    'leverage': 20,
    'stopLossPrice': 110000,
    'takeProfitPrice': 105000,
})
```

## 💥 Create Order Example

```python
from MexcClient import MexcClient

client = MexcClient(api_key=os.getenv('YOUR_U_ID'), is_testnet=True)

order = client.create_order({
    'symbol': 'BTC_USDT',
    'type': 5, # Market
    'side': 3, # Open Short
    'openType': 1, # Isolated
    'vol': 1,
    'leverage': 20,
    'stopLossPrice': 110000,
    'takeProfitPrice': 105000,
})
```

## 💼 Available Methods

| Method | Description |
|--------|-------------|
| [**get_symbols**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-server-time) | Get all available symbols |
| [**get_funding_rate**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-contract-funding-rate) | Get funding rate daat for a symbol |
| [**get_index_price**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-k-line-data-of-the-index-price) | Get K-line data of the index price |
| [**get_ticker_price**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-contract-trend-data) | Get contract trend data |
| [**get_fair_price**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-contract-fair-price) | Get contract fair price |
| [**get_assets**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-all-informations-of-user-39-s-asset) | Get all informations of user's asset |
| [**get_asset_transfer_records**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-user-39-s-asset-transfer-records) | Get the user's asset transfer records |
| [**get_positions_history**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-user-s-history-position-information) | Get the user’s history position information |
| [**get_open_positions**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-user-39-s-current-holding-position) | Get the user's current holding position |
| [**get_open_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-stop-limit-order-list) | Get the user's current pending order |
| [**get_orders_history**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-all-of-the-user-39-s-historical-orders) | Get all of the user's historical orders |
| [**create_order**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#order-under-maintenance) | Create order |
| [**cancel_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#cancel-the-order-under-maintenance) | Cancel the orders |
| [**cancel_all_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#cancel-all-orders-under-a-contract-under-maintenance) | Cancel all uncompleted orders under a contract |
| [**get_trigger_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#gets-the-trigger-order-list) | Gets the trigger order list |
| [**create_trigger_order**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#switch-the-risk-level) | Trigger order |
| [**cancel_trigger_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#cancel-the-trigger-order-under-maintenance) | Cancel the trigger order |
| [**cancel_all_trigger_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#cancel-all-trigger-orders-under-maintenance) | Cancel all trigger orders |
| [**get_stop_limit_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-the-stop-limit-order-list) | Get the Stop-Limit order list |
| [**cancel_stop_limit_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#cancel-the-stop-limit-trigger-order-under-maintenance) | Cancel the Stop-Limit trigger order |
| [**cancel_all_stop_limit_orders**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#cancel-all-stop-limit-price-trigger-orders-under-maintenance) | Cancel all Stop-Limit price trigger orders |
| [**get_risk_limits**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-risk-limits) | Get risk limits |
| [**change_margin**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#increase-or-decrease-margin) | Increase or decrease margin |
| [**get_leverage**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#get-leverage) | Get leverage |
| [**change_leverage**](https://mexcdevelop.github.io/apidocs/contract_v1_en/#switch-leverage) | Switch leverage |
| [**close_all_positions**](https://github.com/verbose0/mexc-api-python) | Close all positions |

## ▶️ Watch Demo Video: placing and cancelling a futures order

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_play_button_icon_%282013%E2%80%932017%29.svg/1280px-YouTube_play_button_icon_%282013%E2%80%932017%29.svg.png" width="100"/>](https://www.youtube.com/watch?v=_GxaLT84f6Y)


## Contact me

<a href="https://t.me/verbose0"><img src="https://img.shields.io/badge/Telegram-2CA5E0?logo=telegram&logoColor=white" title="Telegram"></a>