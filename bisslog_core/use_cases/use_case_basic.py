"""Use case tracking system class implementation"""
from abc import ABC
from typing import Optional


from .use_case_base import UseCaseBase
from ..transactional.transaction_traceable import TransactionTraceable


class BasicUseCase(UseCaseBase, TransactionTraceable, ABC):

    def __init__(self, keyname=None, *, do_trace: bool = True) -> None:
        UseCaseBase.__init__(self, keyname)
        TransactionTraceable.__init__(self)
        self._do_trace = do_trace

    def __call__(self, *args, **kwargs):
        return self._use(*args, **kwargs)

    def __start(self, *args, super_transaction_id: Optional[str] = None, **kwargs) -> Optional[str]:
        if self._do_trace or super_transaction_id is None:
            transaction_id = self._transaction_manager.create_transaction_id(self.keyname)

            self._tracing_opener.start(*args, super_transaction_id=super_transaction_id,
                                       component=self.keyname,
                                       transaction_id=transaction_id, **kwargs)
            return transaction_id
        return super_transaction_id

    def __end(self, transaction_id: str, super_transaction_id: Optional[str], result: object):
        if self._do_trace:
            self._transaction_manager.close_transaction()
            self._tracing_opener.end(transaction_id=transaction_id, component=self.keyname,
                                     super_transaction_id=super_transaction_id, result=result)

    def _use(self, *args, **kwargs):
        """Method to be used as a point before and after the execution of a use case"""

        super_transaction_id = kwargs.pop("transaction_id", None)
        transaction_id = self.__start(*args, super_transaction_id=super_transaction_id, **kwargs)
        if super_transaction_id is None:
            super_transaction_id = transaction_id

        try:
            res = self.use(*args, transaction_id=transaction_id, **kwargs)
            self.__end(transaction_id=transaction_id,
                       super_transaction_id=super_transaction_id, result=res)
        except BaseException as error:
            self.log.tech_error(transaction_id, "use-case-base-catcher", error=error)
            raise
        return res
