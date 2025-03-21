from bisslog_core.adapters.base_adapter import BaseAdapter



class BlankAdapter(BaseAdapter):

    def __init__(self, name_division_not_found: str, original_comp: str):
        self.division_name = name_division_not_found
        self.original_comp = original_comp

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            pass

        def blank_use_of_adapter(*args, **kwargs):
            separator = "#"*80

            self.log.info(
                "\n" + separator + f"\n" +
                f"Blank adapter for {self.original_comp} on division: {self.division_name} \n"
                f"execution of method '{item}' with args {args}, kwargs {kwargs}\n" + separator,
                checkpoint_id="bisslog-blank-division")
        return blank_use_of_adapter
