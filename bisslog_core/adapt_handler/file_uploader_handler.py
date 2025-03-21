from typing import Optional

from bisslog_core.adapt_handler.adapt_handler import AdaptHandler
from bisslog_core.adapters.base_adapter import BaseAdapter
from bisslog_core.ports.upload_file import IUploadFile


class UploadFileHandler(AdaptHandler):
    pass

bisslog_upload_file = UploadFileHandler("file-uploader")
