import sys
import importlib
from unittest.mock import patch, MagicMock


def test_use_case_fallback_mode():
    for name in list(sys.modules):
        if name.startswith("bisslog.use_cases"):
            sys.modules.pop(name)

    with patch("bisslog.use_cases.use_case_decorator.ParamSpec", None), \
         patch("bisslog.use_cases.use_case_decorator.tracing_opener") as tracer, \
         patch("bisslog.use_cases.use_case_decorator.transaction_manager") as txn:

        tracer.start = MagicMock()
        tracer.end = MagicMock()
        txn.create_transaction_id.return_value = "txn-fallback"
        txn.close_transaction = MagicMock()

        use_case_module = importlib.import_module("bisslog.use_cases.use_case_decorator")
        use_case = use_case_module.use_case

        @use_case
        def fallback_func():
            return "fallback ok"

        result = fallback_func()
        assert result == "fallback ok"
        assert getattr(fallback_func, "__is_use_case__", False) is True
        tracer.start.assert_called_once()
        tracer.end.assert_called_once()
        txn.close_transaction.assert_called_once()
