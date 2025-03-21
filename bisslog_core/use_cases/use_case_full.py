from abc import ABC
from typing import Optional

from bisslog_core.adapt_handler.publisher_handler import bisslog_pubsub
from bisslog_core.adapt_handler.file_uploader_handler import bisslog_upload_file
from bisslog_core.use_cases.use_case_basic import BasicUseCase


class FullUseCase(BasicUseCase, ABC):

    __publisher = bisslog_pubsub.main
    __upload_file_adapter = bisslog_upload_file.main

    def publish(self, queue_name: str, body: object, *args, partition: str = None, **kwargs) -> None:
        self.__publisher(queue_name, body, *args, partition=partition, **kwargs)

    def upload_file_stream(self, remote_path: str, stream: bytes, *args,
                           transaction_id: Optional[str] = None, **kwargs) -> bool:
        return self.__upload_file_adapter.upload_file_stream(
            remote_path, stream, *args, transaction_id=transaction_id, **kwargs)

    def upload_file_from_local(self, local_path: str, remote_path: str, *args,
                               transaction_id: Optional[str] = None,  **kwargs) -> bool:
        return self.__upload_file_adapter.upload_file_from_local(
            local_path, remote_path, *args, transaction_id=transaction_id, **kwargs)
