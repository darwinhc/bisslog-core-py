"""Resolve Entrypoint Helper."""
from types import MethodType

from ..use_cases.use_case_decorator.decorator import use_case

def resolve_entrypoint_helper(uc_object):
    """Resolves the method to be used as the use case entrypoint.

    Parameters
    ----------
    uc_object: BasicUseCase

    """
    use_fn = getattr(uc_object, "use", None) or getattr(uc_object, "run", None)
    if use_fn is not None and callable(use_fn):
        # Decorating the use function with @use_case if not already decorated
        use_fn = use_case(keyname=use_fn.__name__, do_trace=uc_object._do_trace)(use_fn)  # pylint: disable=protected-access
        return use_fn

    for attr_name in dir(uc_object):
        if attr_name.startswith("_"):
            continue
        if attr_name in ("entrypoint",):  # avoid recursion
            continue

        attr = getattr(uc_object, attr_name)

        if isinstance(attr, property):
            continue

        if not isinstance(attr, MethodType) or getattr(attr, "__self__", None) is None:
            continue
        func = attr.__func__
        if hasattr(func, "__is_use_case__"):
            # If the function is already decorated with @use_case, return it
            return attr
    raise AttributeError(
        f"No method decorated with @use_case or named 'use'/'run' "
        f"found in {uc_object.__class__.__name__}"
    )
