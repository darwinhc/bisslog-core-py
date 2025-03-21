import logging
from typing import Optional

from bisslog_core.ports.tracing.service_tracer import ServiceTracer


class ServiceTracerLogging(ServiceTracer):

    def __init__(self):
        self._logger = logging.getLogger("service-logger")

    def info(self, payload: object, *args, checkpoint_id: Optional[str] = None,
             extra: dict= None, **kwargs):
        self._logger.info(payload, *args, **kwargs, extra=extra)

    def debug(self, payload: object, *args, checkpoint_id: Optional[str] = None,
              extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.debug(payload, *args, **kwargs)

    def warning(self, payload: object, *args, checkpoint_id: Optional[str] = None,
                extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.warning(payload, *args, **kwargs, extra=extra)

    def error(self, payload: object, *args, checkpoint_id: Optional[str] = None,
              extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.error(payload, *args, **kwargs, extra=extra)

    def critical(self, payload: object, *args, checkpoint_id: Optional[str] = None,
                 extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.critical(payload, *args, **kwargs, extra=extra)

    def func_error(self, payload: object, *args, checkpoint_id: Optional[str] = None,
                   extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.error(payload, *args, **kwargs, extra=extra)

    def tech_error(self, payload: object, *args, checkpoint_id: Optional[str] = None,
                   error: Exception = None, extra: dict = None, **kwargs):
        new_payload: str = str(payload)
        if error is not None:
            new_payload:  str = new_payload + " " + str(error)
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.critical(new_payload, *args, **kwargs, extra=extra)

    def report_start_external(self, payload: object, *args, checkpoint_id: Optional[str] = None,
                              extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.info(payload, *args, **kwargs, extra=extra)

    def report_end_external(self, payload: object, *args, checkpoint_id: Optional[str] = None,
                            extra: dict = None, **kwargs):
        extra = extra or {}
        extra['checkpoint_id'] = checkpoint_id or ''
        extra['transaction_id'] = 'service-logging'
        self._logger.info(payload, *args, **kwargs, extra=extra)
