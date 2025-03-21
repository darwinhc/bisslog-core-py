from bisslog_core.domain_context import domain_context
from bisslog_core.transactional.transaction_manager import TransactionManager, transaction_manager


class TransactionTraceable:

    @property
    def _transaction_manager(self) -> TransactionManager:
        return transaction_manager

    @property
    def log(self):
        return domain_context.tracer

    @property
    def _tracing_opener(self):
        return domain_context.opener
