"""Implementation of the mapping group class"""
from .mapper import Mapper

ERROR = {"target-dup": "The target destination will be overwritten",
         "output-differs": "The types of outputs are different",
         "input-differs": "The types of inputs are different",
         "no-container": "There is nothing in the container"}


class MappingGroup:
    """Container class of mappers that can be run in conjunction with each
    other"""

    def __init__(self, container, resources=None):
        # Checks
        targetKeys = []
        bufferInput = None
        bufferOutput = None
        if not container: raise ValueError(ERROR["no-container"])
        for mapper in container:
            if not isinstance(mapper, Mapper):
                raise ValueError(f'{mapper} is not a mapper')
            if bufferOutput and bufferOutput != mapper.outputType:
                raise ValueError(ERROR['output-differs'] +
                                 f" {bufferOutput} != {mapper.outputType}")
            if bufferInput and bufferInput != mapper.inputType:
                raise ValueError(ERROR['input-differs'] +
                                 f" {bufferInput} != {mapper.inputType}")
            for _, value in mapper.base.items():
                if value in targetKeys: raise ValueError(ERROR["target-dup"])
                targetKeys.append(value)
        self._container = container
        self._resources = resources or {}

    def map(self, data):
        """Map data with multiple mappers"""
        res = self._container[0].map(data)
        for mapper in self._container[1:]:
            res.update(mapper.map(data))
        return res
