# auth.py
"## API Authentication

# This module handles OAuth 2.0 login to the Charles Schwab API.

 import keyring
class Authentication:
    def __init__(self, api-key, api-secret):
        self.api_key = api-key
        self.api_secret = api-secret
        self.token = None
    
    def login(self):
        self.token = keyring.get(self.api_key)
        return self.token
