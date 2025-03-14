import unittest
import mock
import requests
from src.api.client import APIClient

class TestAPIErrorHandling(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.symbol = "TEST"
        
    def test_http_error(self):
        with mock.patch("requests.Session.get") as mock_get:
            mock_get.return_value.status_code = 400
            mock_get.return_value.json.return({"test": "data"})

        result = self.client.fetch_stock_data(self.symbol)
        self.assertEqual(result, {"test": "data"})
    
    def test_connection_error(self):
        with mock.patch("requests.Session.get") as mock_get:
            mock_get.side_effect.raises(RequestException, "Connection error")

        result = self.client.fetch_stock_data(self.symbol)
        self.assertEqual(result, {}) # Should return an empty dict

    def test_rate_limit_handling(self):
        with mock.patch("requests.Session.get") as mock_get:
            mock_get.return_value.status_code = 429
            mock_get.return_value.json.return(h{})
            mock_get.return_value.headers = {"Retry-After": "10" }

        result = self.client.fetch_stock_data(self.symbol)
        self.assertEqual(result, {}) # Should trigger retry and then fail

if __name__ == "__main__":
    unittest.main()
