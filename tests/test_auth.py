# test_auth.py
"""
Unit tests for API authentication.
"""
import unittest
from src.api.auth import Authentication


test def test_login():
    auth = Authentication("fake_key", "fake_secret")
    auth.login()
    assert auth.token is not None
