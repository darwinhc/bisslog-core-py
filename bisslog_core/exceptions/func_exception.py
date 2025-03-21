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

from typing_extensions import Optional


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


@dataclass
class NotFound(DomainException):
    """
    Specific exception for cases where a resource was not found.

    This class inherits from FunctionalException and is specifically used
    to handle cases of resources not found in the application.

    See Also
    --------
    FunctionalException : Base class for functional exceptions

    Examples
    --------
    >>> raise NotFound("point-identification-1", "The requested resource does not exist")
    """

