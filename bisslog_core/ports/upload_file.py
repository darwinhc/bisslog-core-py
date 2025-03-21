from abc import ABC, abstractmethod
from typing import Optional


class IUploadFile(ABC):

    @abstractmethod
    def upload_file_from_local(self, local_path: str, remote_path: str, *args,
                               transaction_id: Optional[str] = None,  **kwargs) -> bool:
        raise NotImplementedError("upload_file_from_local must be implemented")

    @abstractmethod
    def upload_file_stream(self, remote_path: str, stream: bytes, *args,
                           transaction_id: Optional[str] = None, **kwargs) -> bool:
        raise NotImplementedError("upload_file_stream must be implemented")
