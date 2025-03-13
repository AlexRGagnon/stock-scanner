# scanner.py
"## Stock Scanner Module
# This module applies filters to select stocks based on user-defined criteria.

 class StockScanner:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def apply_filters(self, filters):
        # Apply all filters to the stock data
        for key, value in filters.items():
            self.stock_data = [f for f in self.stock_data if f[key] >= value]
        return self.stock_data
