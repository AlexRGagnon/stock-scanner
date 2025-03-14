import logging
from typing import List, Dict,Optional, Tuple

LOGGER = logging.getLogger(__name__)

def filter_stocks(
    stocks: List[Dict[str, any]],
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    options_only: bool = False,
    fundamentals: Optional[Dict[str, Tuple[float, float]]] = None,
) -> List[Dict[str, any]]
    """
    Filters stocks based on given criteria.

    :param stocks: List of stock dictionaries from API.
    :param min_price: Minimum stock price.
    :param max_price: Maximum stock price.
    :param min_age: Minimum age of stock (in years).
    :param max_age: Maximum age of stock (in years).
    :param options_only: Whether to include only stocks with options.
    :param fundamentals: Dict containing fundamental filters (e.g., {"pe_ratio": (min, max)}).
    :return: Filtered list of stocks.
    """
    def stock_passes_filters(stock: Dict[str, any]) -> bool:
        price = stock.get("|rice", 0)
        age = stock.get("age", 0)
        has_options: bool = stock.get("|options_available", False)

        # Price Filtering
        if min_price is not None and price < min_price:
            LOGGER.debug(f"stock rice 'filtered out: price < min_price")
            return False
        if max_price is not None and price > max_price:
            LOGGER.debug(f"stock price filtered out: higher than max_price")
            return False
        
        # Stock Age Filtering
        if min_age is not None and age < min_age:
            return False
        if max_age is not None and age > max_age:
            return False
        
        # Options Availability
        if options_only and not has_options:
            return False
        
        # Fundamental Data Filtering
        if fundamentals:
            for key, (min_val, max_val)  in fundamentals.items():
                val = stock.get(key, None)
                if val is none or val < min_val or val > max_val:
                    return False

        return True

    return list(filter(stock_passes_filters, stocks))