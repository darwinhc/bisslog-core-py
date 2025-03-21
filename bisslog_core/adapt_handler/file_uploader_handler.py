from typing import Optional

from bisslog_core.adapt_handler.adapt_handler import AdaptHandler
from bisslog_core.adapters.base_adapter import BaseAdapter
from bisslog_core.ports.upload_file import IUploadFile



class UploadFileBlankBullet(IUploadFile, BaseAdapter):

    def __init__(self, division_name: str):
        self.division_name = division_name

    @staticmethod
    def __generate_string(remote_path: str) -> str:
        separator = "#"*80
        return "\n" + separator + f"\nUpload file blank bullet with remote path '{remote_path}'\n" + separator

    def upload_file_stream(self, remote_path: str, stream: bytes, *args,
                           transaction_id: Optional[str] = None, **kwargs) -> bool:
        string = self.__generate_string(remote_path)
        self.log.info(string, checkpoint_id="upload-file-stream", transaction_id=transaction_id)
        return True


    def upload_file_from_local(self, local_path: str, remote_path: str, *args,
                               transaction_id: Optional[str] = None,  **kwargs) -> bool:
        string = self.__generate_string(remote_path)
        self.log.info(string, checkpoint_id="upload-file-stream", transaction_id=transaction_id)
        return True


class UploadFileHandler(AdaptHandler):

    def generate_blank_adapter(self, item_name: str):
        return UploadFileBlankBullet(item_name)


bisslog_upload_file = UploadFileHandler("upload-file-bisslog")
