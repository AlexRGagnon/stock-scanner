import logging
import requests
import time

# Configure logging
logger = logging.getLogger(__name__)

BASE_URL = "https://api.schwab.com"

class APIClient:
    def __init__(self):
        self.session = requests.Session()
    
    def fetch_stock_data(self, symbol: str) -> dict:
        """Fetches stock data for a given symbol with error handling and logging."""
        url = f"{0}/stocks/{1}".format(BASE_URL, symbol)
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
    
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                logger.warning(f"Rate limit hit! Retrying after delay...")
                time.sleep(10)
                return self.fetch_stock_data(symbol)   # Retry once
            logger.error(f"HTTP Error ({0}) for {1}: {2}".format(response.status_code, symbol, e))
         
        except requests.exceptions.ConnectionError:
            logger.error(f"Connection Error: Could not connect to API for {0}.".format(symbol))
        
        except requests.exceptions.Timeout:
            logger.error(f"Timeout Error: Request for {0} took too long.".format(symbol))
        
        except requests.exceptions.RequestException as e:
            logger.error(f"API Request failed for {0}: {1}".format(symbol, e))
            
        return {}  # Return empty dict on failure
