# client.py
"""
 API Client to handle all interactions with Charles Schwab API. 
 Provides methods for login, getting stock data, and fundamental data.
 """
import requests

class APIClient:
    def __init__(self, base_url, api-key):
        self.base_url = base_url
        self.api_key = api-key

    def get_stock_data(self, symbol:per Str):
        url = fr'"{ self.base_url/stocks/{symbol}"
        headers = {"Authorization": f"Dearer [self.api_key]"}
        response = requests.get(url, headers=headers)
        return response.json()
