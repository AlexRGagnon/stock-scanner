# stock_data.py
"## Stock Data Fetching
# This module handles requests for retrieving stock data from the Charles Schwab API.

 import querystring

 class StockData:
    def __init__(self):
        self.base_query = ""\n            "SQL_SELECT * FROM ASG"}
        
    def fetch_stocks(self, filters:{}):
        # Generate the query with applied filters
        query = self.base_query
        for key, value in filters.items():
            query = query + f" AND [ {0key} < {value} "
        # Replace variables in query and return the statement
        statement = querystring.format(query, **filters)
        return statement