from abc import ABC, abstractmethod


class IPublisher(ABC):

    @abstractmethod
    def __call__(self, queue_name: str, body: object, partition: str = None, *args, **kwargs) -> None:
        raise NotImplementedError("Method publish must be implemented")
