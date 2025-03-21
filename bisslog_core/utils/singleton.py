from threading import Lock


class SingletonReplaceAttrsMeta(type):

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            new_instance = super().__call__(*args, **kwargs)
            if cls not in cls._instances:
                cls._instances[cls] = new_instance
            else:
                instance = cls._instances[cls]
                new_attrs = cls.get_all_attributes(new_instance)
                for attr in new_attrs:
                    setattr(instance, attr, getattr(new_instance, attr))
        return cls._instances[cls]

    @staticmethod
    def get_all_attributes(new_inst):
        return {key: value for key, value in new_inst.__dict__.items()
                if value is not None and not key.startswith("_")}
