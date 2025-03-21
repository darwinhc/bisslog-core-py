import logging
from typing import Optional

from bisslog_core.ports.tracing.transactional_tracer import TransactionalTracer


class TransactionalTracerLogging(TransactionalTracer):

    def __init__(self):
        self._logger = logging.getLogger("transactional-tracer")

    def info(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict= None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.info(payload, *args, **kwargs, extra=new_extra)

    def debug(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.debug(payload, *args, **kwargs, extra=new_extra)

    def warning(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.warning(payload, *args, **kwargs, extra=new_extra)

    def error(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.error(payload, *args, **kwargs, extra=new_extra)

    def critical(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.critical(payload, *args, **kwargs, extra=new_extra)

    def func_error(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.error(payload, *args, **kwargs, extra=new_extra)

    def tech_error(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, error: Exception = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.critical(payload, *args, **kwargs, extra=new_extra)

    def report_start_external(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.info(payload, *args, **kwargs, extra=new_extra)

    def report_end_external(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        new_extra = self._re_args_with_main(transaction_id, checkpoint_id)
        if extra:
            new_extra.update(extra)
        self._logger.info(payload, *args, **kwargs, extra=new_extra)
