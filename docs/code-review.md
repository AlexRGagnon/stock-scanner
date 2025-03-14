## Code Review - PR #1 - Implement Stock Filtering Feature

### Summary
This PR adds stock filtering functionality in `src/core/filters.py` and unit tests in `tests/test_scanner.py`. The features include:

- Filtering by price range
- Filtering by stock age
- Filtering by options availability
- Filtering by fundamental data (PE ratio, etc.)

### Code Analysis
The new methods are implemented in the `Filters` class.

#### Issues & Improvements

1. **Lack of Type Hints**
   - Solution: Add type annotations for better readability.
   ```python
   def by_price(stocks: list[dict], min_price: float, max_price: float) -> list[dict]:
   ```

2. **Potential KeyError in Filtering**
   - Problem: The function assumes `s["price"]` always exists, which may cause an error.
   - Fix: Use `.get()` to avoid crashes.
   ```python
   if min_price <= s.get("price", 0) <= max_price:
   ```

3. **Inefficient List Comprehension**
   - Suggestion: Use a filter function for readability.
   ```python
   return list(filter(lambda s: min_price <= s.get("price", 0) <= max_price, stocks))
   ```

4. **Expandability**
   - Consider refactoring `Filters` to be more modular and support dynamic filtering.

### Unit Tests

- Added tests for fundamental filters.
- Checked for missing stock keys.
- Included negative and extreme value cases.

### Security & Performance Review

- Checked for **hardcoded values** or **invalid input handling**.
- Logging added for debugging potential filter failures.
- Security checks added for missing stock keys.

### Status - REQUESTING CHANGES

