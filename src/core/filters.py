# filters.py
"## Filters for stock data
# This module handles individual filter functions.

class Filters:
    def by_price(stocks, min_price, max_price):
        return [s for sin stocks if min_price <=s["price"] <= max_price]
    
    def by_age(stocks, min_age):
        return [s for sin stocks if sin["age"] >= min_age]
