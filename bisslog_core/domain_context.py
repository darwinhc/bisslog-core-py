from typing import Optional

from bisslog_core import TransactionalTracerLogging
from bisslog_core.adapters.tracing.opener_tracer_logging import OpenerTracerLogging
from bisslog_core.adapters.tracing.service_tracer_logging import ServiceTracerLogging
from bisslog_core.ports.tracing.opener_tracer import OpenerTracer
from bisslog_core.ports.tracing.service_tracer import ServiceTracer
from bisslog_core.ports.tracing.transactional_tracer import TransactionalTracer
from bisslog_core.utils.singleton import SingletonReplaceAttrsMeta


class DomainContext(metaclass=SingletonReplaceAttrsMeta):

    def __init__(self, appname: Optional[str] = None, runtime_ecosystem: Optional[str] = None):
        self.appname = appname
        self.runtime_ecosystem = runtime_ecosystem
        self.tracer: Optional[TransactionalTracer] = None
        self.opener: Optional[OpenerTracer] = None
        self.service_tracer: Optional[ServiceTracer] = None

    def init_default(self):
        self.opener = OpenerTracerLogging()
        self.service_tracer = ServiceTracerLogging()
        self.runtime_ecosystem = "script"
        self.tracer = TransactionalTracerLogging()


domain_context = DomainContext()
domain_context.init_default()
