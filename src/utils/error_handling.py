# error_handling.py
"""
# Error handling for the application.

"""

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
