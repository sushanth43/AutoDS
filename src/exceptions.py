"""
Custom exceptions for AutoDS.
"""

class AutoDSError(Exception):
    """
    Base exception class for AutoDS.

    All custom exceptions in this project should inherit from this class.
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class DatasetNotFoundError(AutoDSError):
    """
    Raised when the required dataset cannot be found.
    """
    pass