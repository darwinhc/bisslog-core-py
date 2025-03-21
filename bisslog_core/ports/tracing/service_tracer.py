from abc import ABC

from bisslog_core.ports.tracing.tracer import Tracer


class ServiceTracer(Tracer, ABC):
    pass
