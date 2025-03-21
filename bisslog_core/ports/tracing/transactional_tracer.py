from abc import abstractmethod, ABC
from typing import Optional


from bisslog_core.transactional.transaction_manager import TransactionManager, transaction_manager
from bisslog_core.ports.tracing.tracer import Tracer


class TransactionalTracer(Tracer, ABC):

    @property
    def _transaction_manager(self) -> TransactionManager:
        return transaction_manager

    def _re_args_with_main(self, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None) -> dict:
        if transaction_id is None:
            transaction_id = self._transaction_manager.get_main_transaction_id()
        if checkpoint_id is None or not checkpoint_id:
            checkpoint_id = ""
        return {"transaction_id": transaction_id, "checkpoint_id": checkpoint_id}

    def _re_args_with_current(self, transaction_id: Optional[str] = None,
                              checkpoint_id: Optional[str] = None) -> dict:
        if transaction_id is None:
            transaction_id = self._transaction_manager.get_transaction_id()
        if checkpoint_id is None or not checkpoint_id:
            checkpoint_id = ""
        return {"transaction_id": transaction_id, "checkpoint_id": checkpoint_id}

    @abstractmethod
    def func_error(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method func_error")

    @abstractmethod
    def tech_error(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method tech_error")

    @abstractmethod
    def report_start_external(self, payload: object, *args, transaction_id: Optional[str] = None,
                              checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method report_start_external")

    @abstractmethod
    def report_end_external(self, payload: object, *args, transaction_id: Optional[str] = None,
                 checkpoint_id: Optional[str] = None, extra: dict = None, **kwargs):
        raise NotImplementedError("TracingManager must implement method report_end_external")
