"""Opener Tracer Logging."""

import logging
from typing import Optional

from bisslog_core.ports.tracing.opener_tracer import OpenerTracer


class OpenerTracerLogging(OpenerTracer):
    """
    A logging-based implementation of `OpenerTracer`.

    This class logs the start and end of operations with transaction details,
    facilitating debugging and tracing in distributed systems.

    Attributes
    ----------
    _logger : Logger
        Object Logger instance used for tracing messages.

    Methods
    -------
    start(*args, transaction_id, component, super_transaction_id=None, **kwargs)
        Logs the start of an operation.

    end(*args, transaction_id, component, super_transaction_id, result=None)
        Logs the end of an operation, including the result.
    """

    def __init__(self):
        """
        Initializes the logger for tracing operations.
        """
        self._logger = logging.getLogger("opener-logger")

    def start(self, *args, transaction_id: str, component: str,
              super_transaction_id: Optional[str] = None, **kwargs):
        """
        Logs the start of an operation.

        Parameters
        ----------
        transaction_id : str
            The unique identifier for the transaction.
        component : str
            The component initiating the operation.
        super_transaction_id : Optional[str], default=None
            The parent transaction ID, if applicable.
        """
        extra = {'checkpoint_id': "start-" + component, 'transaction_id': transaction_id}
        super_transaction_id = super_transaction_id or ''
        self._logger.debug(super_transaction_id, extra=extra)

    def end(self, *args, transaction_id: Optional[str], component: str,
            super_transaction_id: Optional[str], result: object = None):
        """
        Logs the end of an operation, including the result.

        Parameters
        ----------
        transaction_id : Optional[str]
            The unique identifier for the transaction.
        component : str
            The component that completed the operation.
        super_transaction_id : Optional[str]
            The parent transaction ID, if applicable.
        result : object, default=None
            The result of the operation, if available.
        """
        extra = {'checkpoint_id': "end-" + component, 'transaction_id': transaction_id}
        super_transaction_id = super_transaction_id or ''
        self._logger.debug("%s with result %s", super_transaction_id, result, extra=extra)
