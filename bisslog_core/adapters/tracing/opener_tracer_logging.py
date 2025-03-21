import logging
from typing import Optional

from bisslog_core.ports.tracing.opener_tracer import OpenerTracer


class OpenerTracerLogging(OpenerTracer):

    def __init__(self):
        self._logger = logging.getLogger("opener-logger")

    def start(self, *args, transaction_id: str, component: str,
              super_transaction_id: Optional[str] = None, **kwargs):

        extra = {'checkpoint_id': "start-" + component, 'transaction_id': transaction_id}
        super_transaction_id = super_transaction_id or ''
        self._logger.debug(f"{super_transaction_id}", extra=extra)

    def end(self, *args, transaction_id: Optional[str], component: str, super_transaction_id: Optional[str],
            result: object = None):
        extra = {'checkpoint_id': "end-"+component, 'transaction_id': transaction_id}
        super_transaction_id = super_transaction_id or ''
        self._logger.debug(f"{super_transaction_id} with result {result}", extra=extra)
