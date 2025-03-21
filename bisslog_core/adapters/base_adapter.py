from abc import ABC

from bisslog_core.transactional.transaction_traceable import TransactionTraceable


class BaseAdapter(TransactionTraceable, ABC):
    pass
