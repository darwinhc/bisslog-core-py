from dataclasses import dataclass
from typing import Optional

from bisslog_core.exceptions.func_exception import DomainException


@dataclass
class HttpCodedException(DomainException):
    """
    Specific exception for cases where HTTP code can be set for indicate status of operation.

    This class inherits from FunctionalException and is specifically used.

    See Also
    --------
    FunctionalException : Base class for functional exceptions

    Examples
    --------
    >>> raise HttpCodedException("HTTP_CODE", "The HTTP code has been set")
    """
    http_code: int = 400
    message: Optional[str] = None

    def __post_init__(self):
        if 400 <= self.http_code < 599:
            raise ValueError("http_code must be a valid HTTP code error")



@dataclass
class HttpCodedClientException(HttpCodedException):
    """
    Specific exception for cases where HTTP code can be set for indicate status of client.
    """


@dataclass
class HttpCodedServerSideException(HttpCodedClientException):
    """
    Specific exception for cases where HTTP code can be set for indicate status of server.
    """


