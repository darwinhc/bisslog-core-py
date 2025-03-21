from abc import abstractmethod, ABC
from typing import Optional



class Tracer(ABC):

    @abstractmethod
    def info(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method info")

    @abstractmethod
    def debug(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method debug")

    @abstractmethod
    def warning(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method warning")

    @abstractmethod
    def error(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method error")

    @abstractmethod
    def critical(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method critical")
