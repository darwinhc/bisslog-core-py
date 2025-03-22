"""Module defining the abstract OpenerTracer class for transaction tracing."""

from abc import ABC, abstractmethod


class OpenerTracer(ABC):
    """Abstract base class for tracing the start and end of transactions.

    This class defines methods for tracking when a transaction starts and ends,
    ensuring structured logging and traceability."""

    @abstractmethod
    def start(self, *args, transaction_id: str, component: str,
              super_transaction_id: str|None = None, **kwargs):
        """Marks the start of a transaction.

        Parameters
        ----------
        transaction_id : str
            The unique identifier of the transaction.
        component : str
            The name of the component initiating the transaction.
        super_transaction_id : str, optional
            The identifier of a parent transaction, if applicable."""
        raise NotImplementedError("TracingOpener must implement start")

    @abstractmethod
    def end(self, *args, transaction_id: str|None, component: str,
            super_transaction_id: str|None, result: object = None):
        """Marks the end of a transaction.

        Parameters
        ----------
        transaction_id : str, optional
            The unique identifier of the transaction.
        component : str
            The name of the component that executed the transaction.
        super_transaction_id : str, optional
            The identifier of a parent transaction, if applicable.
        result : object, optional
            The result or output of the transaction, if any."""
        raise NotImplementedError("TracingOpener must implement end")
