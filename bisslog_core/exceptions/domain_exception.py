"""Functional exception module.

This module defines custom exceptions for handling functional errors
in a structured way throughout the application.

Classes
-------
FunctionalException
    Base exception class for functional errors
FunctionalNotFoundException
    Exception for handling not found resources
"""

from dataclasses import dataclass



@dataclass
class DomainException(Exception):
    """Base exception for functional errors in the application.

    This class extends Exception and uses dataclass to provide
    a consistent structure for functional exceptions.

    Parameters
    ----------
    keyname : str
        Unique identifier for the functional error
    message : str
        Descriptive error message

    Attributes
    ----------
    keyname : str
        Unique identifier for the functional error
    message : str
        Descriptive error message

    Examples
    --------
    >>> raise DomainException("error-key", "Error description")
    """
    keyname: str
    message: str


class NotFound(DomainException):
    pass

class NotAllowed(DomainException):
    pass

