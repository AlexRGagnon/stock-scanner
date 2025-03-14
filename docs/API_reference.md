# **API Reference (`API_reference.md`)**  

## **📍 Overview**  
This document provides a comprehensive reference for interacting with the **Charles Schwab API**, detailing authentication methods, key endpoints, required parameters, and expected responses.  

---

## **📌 Authentication**  
The API uses **OAuth 2.0** for authentication. The authentication process involves:  
1. **Requesting an authorization code** from the API.  
2. **Exchanging the code for an access token**.  
3. **Refreshing the access token** when it expires.  

### **🔹 OAuth 2.0 Authentication Flow**  
- **Authorization URL:**  
  ```
  https://api.schwab.com/v1/oauth/authorize
  ```
- **Token Exchange URL:**  
  ```
  https://api.schwab.com/v1/oauth/token
  ```
- **Required Parameters for Token Request:**  
  | Parameter       | Description |
  |---------------|-------------|
  | `client_id`   | Your API key |
  | `client_secret` | Your API secret |
  | `code`        | Authorization code received from OAuth login |
  | `redirect_uri` | Must match the registered callback URL (`https://127.0.0.1`) |
  | `grant_type`  | Must be `authorization_code` |

- **Example Response (Access Token Exchange):**  
  ```json
  {
    "access_token": "abc123xyz",
    "expires_in": 3600,
    "refresh_token": "refresh123xyz",
    "token_type": "Bearer"
  }
  ```

---

## **📌 Endpoints**  

### **1️⃣ Get Stock Price**  
- **URL:**  
  ```
  GET /quotes/stock/price/{symbol}
  ```
- **Parameters:**  
  | Parameter  | Type   | Description |
  |-----------|--------|-------------|
  | `symbol`  | string | Stock ticker (e.g., `AAPL`, `GOOGL`) |

- **Example Response:**  
  ```json
  {
    "symbol": "AAPL",
    "price": 150.25,
    "currency": "USD",
    "timestamp": "2024-03-12T14:30:00Z"
  }
  ```

---

### **2️⃣ Get Stock Fundamental Data**  
- **URL:**  
  ```
  GET /quotes/fundamental/{symbol}
  ```
- **Parameters:**  
  | Parameter  | Type   | Description |
  |-----------|--------|-------------|
  | `symbol`  | string | Stock ticker |

- **Example Response:**  
  ```json
  {
    "symbol": "AAPL",
    "pe_ratio": 28.5,
    "ps_ratio": 7.2,
    "revenue": 394.3,
    "debt": 98.6,
    "free_cash_flow": 73.2
  }
  ```

---

### **3️⃣ Get Options Data**  
- **URL:**  
  ```
  GET /options/{symbol}
  ```
- **Parameters:**  
  | Parameter  | Type   | Description |
  |-----------|--------|-------------|
  | `symbol`  | string | Stock ticker |

- **Example Response:**  
  ```json
  {
    "symbol": "AAPL",
    "options": [
      {
        "expiration": "2024-03-15",
        "strike": 150,
        "type": "CALL",
        "price": 2.50
      },
      {
        "expiration": "2024-03-22",
        "strike": 155,
        "type": "PUT",
        "price": 3.75
      }
    ]
  }
  ```

---

## **📌 API Rate Limits & Best Practices**  
- **Maximum requests per minute:** `120`  
- **Use caching where possible to reduce duplicate requests.**  
- **Batch requests when fetching multiple stocks to improve efficiency.**  
- **Implement error handling for rate limit exceedance (`429 Too Many Requests`).**  

---

## **📌 Error Handling**  
| HTTP Status | Meaning |
|-------------|---------|
| `200 OK` | Request successful |
| `400 Bad Request` | Invalid parameters |
| `401 Unauthorized` | Invalid or expired token |
| `403 Forbidden` | API key does not have access |
| `429 Too Many Requests` | Rate limit exceeded |
| `500 Internal Server Error` | API server issue |

---

## **📌 API Checklist for Developers**  
✅ **Obtain and securely store API credentials.**  
✅ **Use OAuth 2.0 authentication to get an access token.**  
✅ **Ensure API requests handle rate limits properly.**  
✅ **Retrieve stock data efficiently using batch requests.**  
✅ **Monitor for API changes and update integration accordingly.**  

---

🚀 **This document serves as the go-to reference for integrating and troubleshooting the Stock Scanner’s API calls.**  
