from abc import ABC, abstractmethod


class INotifier(ABC):

    @abstractmethod
    def __call__(self, notification_obj: object) -> None:
        raise NotImplementedError("Callable must be implemented")
