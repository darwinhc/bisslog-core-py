"""Module providing logging-based implementation of the TransactionalTracer interface."""

import logging

from bisslog_core.ports.tracing.transactional_tracer import TransactionalTracer


class TransactionalTracerLogging(TransactionalTracer):
    """Implementation of TransactionalTracer that logs messages using Python's logging module."""

    def __init__(self):
        self._logger = logging.getLogger("transactional-tracer")

    def info(self, payload: object, *args, transaction_id: str|None = None,
             checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs an informational message.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None."""
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.info(payload, *args, **kwargs, extra=new_extra)

    def debug(self, payload: object, *args, transaction_id: str|None = None,
              checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs a debug message.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None.        """
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.debug(payload, *args, **kwargs, extra=new_extra)

    def warning(self, payload: object, *args, transaction_id: str|None = None,
                checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs a warning message.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None.        """
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.warning(payload, *args, **kwargs, extra=new_extra)

    def error(self, payload: object, *args, transaction_id: str|None = None,
              checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs an error message.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None.        """
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.error(payload, *args, **kwargs, extra=new_extra)

    def critical(self, payload: object, *args, transaction_id: str|None = None,
                 checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs a critical error message.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None.        """
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.critical(payload, *args, **kwargs, extra=new_extra)

    def func_error(self, payload: object, *args, transaction_id: str|None = None,
                   checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs a function-related error message.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None.        """
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.error(payload, *args, **kwargs, extra=new_extra)

    def tech_error(self, payload: object, *args, transaction_id: str|None = None,
                   checkpoint_id: str|None = None, error: Exception = None, extra: dict = None,
                   **kwargs):
        """Logs a technical error message, optionally including an exception.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None.
        error: Exception
            Captured error to be logged."""
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        error_payload = ""
        if isinstance(error, Exception):
            error_payload = ":" + str(error)

        self._logger.critical(str(payload) + error_payload , *args, **kwargs, extra=new_extra)

    def report_start_external(self, payload: object, *args, transaction_id: str|None = None,
                              checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs the start of an external operation.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None."""
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.info(payload, *args, **kwargs, extra=new_extra)

    def report_end_external(self, payload: object, *args, transaction_id: str|None = None,
                            checkpoint_id: str|None = None, extra: dict = None, **kwargs):
        """Logs the end of an external operation.

        Parameters
        ----------
        payload : object
            The message or object to log.
        transaction_id : str|None, optional
            An identifier for the transaction, by default None.
        checkpoint_id : str|None, optional
            An identifier for the logging checkpoint, by default None.
        extra : dict, optional
            Additional logging context, by default None."""
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.info(payload, *args, **kwargs, extra=new_extra)
