"""Use Case Entry Resolver definition."""
from abc import ABCMeta
from typing import Optional

from .use_case_base import UseCaseBase
from ..transactional.transaction_traceable import TransactionTraceable
from ..utils.resolve_entrypoint_helper import resolve_entrypoint_helper


class UseCaseEntryResolver(UseCaseBase, TransactionTraceable, metaclass=ABCMeta):
    """Abstract base class for use case entry resolvers."""

    def __init__(self, keyname: Optional[str] = None, *, do_trace: bool = True) -> None:
        UseCaseBase.__init__(self, keyname)
        self._do_trace = do_trace
        self._entrypoint = resolve_entrypoint_helper(self)
