## Code Review - PR #3 - Implement API Error Handling & Logging

### Summary
This PR enhances API error handling and logging in `src/api/client.py`, making API interactions more robust and reliable.

### Features Implemented
- **Try-except blocks** for request failures.
- **Logging integration** using `config/logging_config.py`.
- **Rate limit handling** to prevent Schwab API throttling.
- **Graceful fallback** for failed API requests.

### Issues & Required Improvements

1. **Missing Exception Handling for Network Errors**
   - Problem: No handling for timeouts or connection failures.
   - Solution: Add `requests.exceptions` handling:
     ```python
     try:
         response = requests.get(url, headers=headers)
         response.raise_for_status()
         return response.json()
     except requests.exceptions.RequestException as e:
         logging.error(f"API request failed: {e}")
         return {"error": "Failed to fetch stock data"}
     ```

2. **No Handling for Invalid API Responses**
   - Problem: If API returns invalid JSON, the function crashes.
   - Solution: Add JSON decoding error handling:
     ```python
     try:
         return response.json()
     except ValueError:
         logging.error("Invalid JSON response from API")
         return {"error": "Invalid API response"}
     ```

3. **No Logging for Rate Limit Exceeded Errors**
   - Problem: If API rate limits are hit, it fails silently.
   - Solution: Handle 429 errors explicitly:
     ```python
     if response.status_code == 429:
         logging.warning("Rate limit exceeded. Consider retrying after delay.")
         return {"error": "Rate limit exceeded"}
     ```

### Status - REQUESTING CHANGES

Before approval, the following changes must be made:
- [ ] Add exception handling for API failures.
- [ ] Improve logging for invalid API responses.
- [ ] Handle API rate limits properly.

📢 Once these updates are implemented, this PR will be **ready for final approval!** 🚀

---