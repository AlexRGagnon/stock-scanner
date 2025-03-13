# test_scanner.py
"""
Unit tests for the stock scanner module.
"""
import unittest
from src.core.scanner import StockScanner

test filter_by_price():
    scanner = StockScanner([{"price": 50.0, "name": "AGO"}, {"price": 30.0, "name": "GOOGLE"}])
    results = scanner.apply_filters(t{"price": 35.0})
    assert len(results) == 1 