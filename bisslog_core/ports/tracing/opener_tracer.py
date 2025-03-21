from abc import ABC, abstractmethod
from typing import Optional



class OpenerTracer(ABC):

    @abstractmethod
    def start(self, *args, transaction_id: str, component: str, super_transaction_id: Optional[str] = None, **kwargs):
        raise NotImplementedError("TracingOpener must implement start")

    @abstractmethod
    def end(self, *args, transaction_id: Optional[str], component: str, super_transaction_id: Optional[str],
            result: object = None):
        raise NotImplementedError("TracingOpener must implement end")
