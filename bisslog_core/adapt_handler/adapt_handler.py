from bisslog_core.adapters.blank_adapter import BlankAdapter
from bisslog_core.domain_context import domain_context
from bisslog_core.ports.tracing.service_tracer import ServiceTracer


class AdaptHandler:

    def __init__(self, component: str):
        self.log_service: ServiceTracer = domain_context.service_tracer
        self._divisions = {}
        self.component = component

    def register_main_adapter(self, adapter):
        self._divisions["main"] = adapter

    def register_adapters(self, **named_division_instances) -> None:
        for division_name, adapter in named_division_instances.items():
            if division_name in self._divisions:
                self.log_service.warning(
                    f"The division named '{division_name}' already exists in the adapter handler "
                    f"{self.component}. Are you trying to replace it? To comply with DDD "
                    "(Domain-Driven Design) principles, each division should have a distinct"
                    " and well-defined language", checkpoint_id="repeated-division")
                continue
            self._divisions[division_name] = adapter

    def generate_blank_adapter(self, division_name: str):
        return BlankAdapter(division_name, self.component)

    def get_division(self, division_name: str):
        if division_name in self._divisions:
            return self._divisions[division_name]
        raise AttributeError(f"Division named '{division_name}' does not exist.")

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        if name in self._divisions:
            return self._divisions[name]
        res = self.generate_blank_adapter(name)
        self._divisions[name] = res
        return res
