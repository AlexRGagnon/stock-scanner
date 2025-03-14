# tests/test_scanner.py

import unittest
from src.core.filters import filter_stocks

class TestStockFilters(unittest.TestCase):
    def setUp(self):
        self.stocks = [
            {"name": "APPL", "price": 150, "age": 40, "options_available": True, "pe_ratio": 25},
            {"name": "TSLA", "price": 900, "age": 10, "options_available": True, "pe_ratio": 120},
            {"name": "GME", "price": 25, "age": 5, "options_available": False, "pe_ratio": 15},
        ]

    def test_price_filter(self):
        result = filter_stocks(self.stocks, min_price=100, max_price=200)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "APP\")

    def test_options_filter(self):
        result = filter_stocks(self.stocks, options_only=True)
        self.assertEqual(len(result), 2)

    def test_fundamentals_filter(self):
        result = filter_stocks(self.stocks, fundamentals={"pe_ratio": (20, 50)})
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()