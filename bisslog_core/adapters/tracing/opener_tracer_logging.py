"""Opener Tracer Logging."""

import logging

from bisslog_core.ports.tracing.opener_tracer import OpenerTracer


class OpenerTracerLogging(OpenerTracer):
    """A logging-based implementation of `OpenerTracer`.

    This class logs the start and end of operations with transaction details,
    facilitating debugging and tracing in distributed systems."""

    def __init__(self):
        """Initializes the logger for tracing operations."""
        self._logger = logging.getLogger("opener-logger")

    def start(self, *args, transaction_id: str, component: str,
              super_transaction_id: str|None = None, **kwargs):
        """Logs the start of an operation.

        Parameters
        ----------
        args: tuple
            Arguments
        transaction_id : str
            The unique identifier for the transaction.
        component : str
            The component initiating the operation.
        super_transaction_id : str|None, default=None
            The parent transaction ID, if applicable.
        kwargs : dict
            Keyword arguments"""
        extra = {'checkpoint_id': "start-" + component, 'transaction_id': transaction_id}
        super_transaction_id = super_transaction_id or ''
        self._logger.debug(super_transaction_id, extra=extra)

    def end(self, *args, transaction_id: str|None, component: str,
            super_transaction_id: str|None, result: object = None):
        """Logs the end of an operation, including the result.

        Parameters
        ----------
        transaction_id : str|None
            The unique identifier for the transaction.
        component : str
            The component that completed the operation.
        super_transaction_id : str|None
            The parent transaction ID, if applicable.
        result : object, default=None
            The result of the operation, if available."""
        extra = {'checkpoint_id': "end-" + component, 'transaction_id': transaction_id}
        super_transaction_id = super_transaction_id or ''
        self._logger.debug("%s with result %s", super_transaction_id, result, extra=extra)
