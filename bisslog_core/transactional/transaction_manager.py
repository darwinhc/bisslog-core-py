import threading
import uuid
from dataclasses import dataclass
from typing import Dict, List

from bisslog_core.utils.singleton import SingletonReplaceAttrsMeta


@dataclass
class Transaction:
    transaction_id: str
    component: str


class TransactionManager(metaclass=SingletonReplaceAttrsMeta):

    def __init__(self):
        # Cache transactions
        self._thread_active_transaction_mapping: Dict[int, List[Transaction]] = {}
        self._loc = threading.Lock()

    @staticmethod
    def get_thread_id() -> int:
        return threading.get_ident()

    def create_transaction_id(self, component: str) -> str:
        """
        Create a new unique transaction identifier and saved.

        Returns
        -------
        str
            New UUID as string
        """
        transaction_id = str(uuid.uuid4())
        with self._loc:
            thread_id = self.get_thread_id()
            if thread_id not in self._thread_active_transaction_mapping:
                self._thread_active_transaction_mapping[thread_id] = [Transaction(transaction_id, component)]
            else:
                transactions_ids: list = self._thread_active_transaction_mapping[thread_id]
                transactions_ids.append(Transaction(transaction_id, component))
        return transaction_id

    def get_transaction_id(self) -> str:
        with self._loc:
            thread_id = self.get_thread_id()
            if (
                    thread_id in self._thread_active_transaction_mapping and
                    self._thread_active_transaction_mapping[thread_id]
            ):
                return self._thread_active_transaction_mapping[thread_id][-1].transaction_id
            else:
                raise KeyError("Transaction ID not found in cache")

    def get_component(self) -> str:
        with self._loc:
            thread_id = self.get_thread_id()
            if (
                    thread_id in self._thread_active_transaction_mapping and
                    self._thread_active_transaction_mapping[thread_id]
            ):
                return self._thread_active_transaction_mapping[thread_id][-1].component
            else:
                raise KeyError("Transaction ID not found in cache")

    def get_main_transaction_id(self) -> str:
        with self._loc:
            thread_id = self.get_thread_id()
            if (
                    thread_id in self._thread_active_transaction_mapping and
                    self._thread_active_transaction_mapping[thread_id]
            ):
                return self._thread_active_transaction_mapping[thread_id][0].transaction_id
            else:
                raise KeyError("Transaction ID not found in cache")

    def close_transaction(self):
        self._thread_active_transaction_mapping[self.get_thread_id()].pop()

    def clear(self):
        with self._loc:
            self._thread_active_transaction_mapping.clear()


transaction_manager = TransactionManager()
