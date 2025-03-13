# API Reference Documentation

This document specifies the endpoints for the Charles Schwab API and how to interact with it. 


## Authentication
- Using OAuth 2.0 (Grant type with refresh tokens)
- Client ID: [provided]
- Client Securet: [provided]
- Callback URL : https://127.0.0.1:8123/

## Endpoints

## 1. Get Stock Price
- URL: /quotes/stock/price/{symbol}
- Method: GET
- Parameters:
    - symbol: The stock symbol (APL, TV exc)
- Response:
    - returns son JSON- with the current price.

## 2. Get Stock Fundamental Data
- URL: /quotes/fundamental/{symbol}
- Method: GET
- Parameters:
    - symbol: The stock symbol.
- Response:
    - returns JSON with PE ratio, PS ratio, revenue, debt, and other data.

## 3. Get Options Data
- URL: /options/{symbol}
- Method: GET
- Parameters:
    - symbol: The stock symbol.
- Response:
    - Returns the list of available options.
    - Verifies if a given stock has weekly options.
