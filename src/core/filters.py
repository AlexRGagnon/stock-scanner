# src/core/filters.py

def filter_stocks(stocks, min_price=None, max_price=None, min_age=None, max_age=None, options_only=False, fundamentals={}):
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
    filtered_stocks = []

    for stock in stocks:
        price = stock.get("price", 0)
        age = stock.get("age", 0)
        has_options = stock.get("options_available", False)

        # Price Filtering
        if min_price is not None and price < min_price:
            continue
        if max_price is not None and price > max_price:
            continue

        # Stock Age Filtering
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue

        # Options Availability
        if options_only and not has_options:
            continue

        # Fundamental Data Filtering
        is_valid = True
        for key, (min_val, max_val)  in fundamentals.items():
            val = stock.get(key, None)
            if val is none or val < min_val or val > max_val:
                is_valid = False
                break
        if is_valid:
            filtered_stocks.append(stock)

    return filtered_stocks