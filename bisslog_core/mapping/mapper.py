"""Implementation of the general mapper class"""
from .arranger import IArranger

ERRORS = {
    "base-type-error": "Base must be a dictionary or list",
    "base-kv-type-error": "Base must be a dict with key-value string",
    "no-values": "There is not key or value",
    "no-route": "There is not route or path",
    "no-base": "There is not base",
    "path-naming-incorrect": "Resources to be added in the path naming are missing"
}


class Mapper(IArranger):
    """Redirector of information to specific fields and combiner of these fields"""

    defaultSeparator = '.'
    listIdentifier = '[]'
    _defaultPathNaming = '$'

    def __init__(self, name: str, base: dict, inputType: str = "dict", outputType: str = "dict",
                 resources: dict = None, *_, **kwargs):
        super().__init__()
        if isinstance(base, dict):
            for key, value in base.items():
                self.__checkSourceTarget(key, value)
        elif isinstance(base, list):
            for obj in base:
                self.__checkSourceTarget(obj.get("from"), obj.get("to"))
        else:
            raise TypeError(ERRORS["base-type-error"])

        self._name = name
        self._inputType = inputType
        self._outputType = outputType
        self._resources = resources or {}
        self._separator = kwargs.get('separator') or self.defaultSeparator
        self._pathNaming = kwargs.get('pathNaming') or self._defaultPathNaming
        if isinstance(base, dict):
            self.__format = "dict"
        else:
            self.__format = "list"

        if isinstance(base, dict):  # base as dict
            baseCopy = base.copy()
            for pathSource, pathTarget in baseCopy.items():
                newPathSource, newPathTarget = self.__checkResourcesAndReplace(pathSource,
                                                                               pathTarget)
                del base[pathSource]
                base[newPathSource] = newPathTarget
        else:  # base as list
            baseCopy = base.copy()
            for i, obj in enumerate(baseCopy):
                pathSource, pathTarget = obj["from"], obj["to"]
                newPathSource, newPathTarget = self.__checkResourcesAndReplace(pathSource,
                                                                               pathTarget)
                base[i]["from"] = newPathSource
                base[i]["to"] = newPathTarget
        self._base = base

    @staticmethod
    def __checkSourceTarget(source, target):
        """Performs various validations of data paths

        Parameters
        ----------
        source: str
        target: str
        """
        if not isinstance(source, str):
            raise TypeError(f'{ERRORS["base-kv-type-error"]} in key {source}')
        if not source or not target:
            raise ValueError(ERRORS["no-values"])
        if not isinstance(target, str):
            raise TypeError(ERRORS["base-kv-type-error"] + " in value of key " + str(source))

    def __checkResourcesAndReplace(self, pathSource, pathTarget):
        """Validates and performs the loading process in the paths and the associated resources.

        Parameters
        ----------
        pathSource: str
        pathTarget: str

        Returns
        -------
        newPathSource: str
        newPathTarget: str
        """
        newPathSource, newPathTarget = pathSource, pathTarget
        for key in self._resources:
            newPathSource = newPathSource.replace(self._pathNaming + key, self._resources[key])
            newPathTarget = newPathTarget.replace(self._pathNaming + key, self._resources[key])
        if self._pathNaming in newPathSource or self._pathNaming in newPathTarget:
            raise ValueError(ERRORS["path-naming-incorrect"])
        return newPathSource, newPathTarget

    @property
    def base(self) -> dict:
        """Getter of the base property"""
        return self._base

    @property
    def name(self) -> str:
        """Getter of the name property"""
        return self._name

    @property
    def inputType(self) -> str:
        """Getter of the input type property"""
        return self._inputType

    @property
    def outputType(self) -> str:
        """Getter of the output type property"""
        return self._outputType

    def getInitialObject(self):
        """Get the initial object as buffer to return"""
        res = None
        if self._outputType == "dict":
            res = {}
        elif self._outputType == "list":
            res = []
        return res

    def __execute__(self, data=None):
        """Makes use of the entered data to perform the mapping of incoming data

        Parameters
        ----------
        data: dict, list
            Source data from which the information will be obtained

        Returns
        -------
        res: dict, list
            Data object mapped from the source
        """
        if self.__format == "dict": res = self.__executeMapperAsDict(data)
        else: res = self.__executeMapperAsList(data)
        return res

    def __set_buffer(self, target: str, initial: list | dict, buffer):
        route = target.split(self._separator)
        bufferTarget = initial
        while len(route) >= 1:
            path = route.pop(0)
            if not route:
                bufferTarget[path] = buffer
            elif path in bufferTarget:
                bufferTarget = bufferTarget[path]
            elif path not in bufferTarget:
                bufferTarget[path] = {}
                bufferTarget = bufferTarget[path]

    def __executeMapperAsDict(self, data):
        """Performs mapping of data from a base as a dict"""
        res = self.getInitialObject()
        for source, target in self._base.items():
            route = source.split(self._separator)
            buffer = data.get(route[0], {})
            for pathI in route[1:]:
                if pathI in buffer: buffer = buffer[pathI]
                else:
                    buffer = None
                    break
            self.__set_buffer(target, res, buffer)
        return res

    def __executeMapperAsList(self, data):
        """Performs mapping of data from a base as a list"""
        res = self.getInitialObject()
        self._base : list
        for obj in self._base:
            source, target = obj["from"], obj["to"]
            route = source.split(self._separator)
            buffer = data.get(route[0], {})
            for pathI in route[1:]:
                if pathI in buffer:
                    buffer = buffer[pathI]
                else:
                    buffer = None
                    break
            buffer = self.arrangeValue(buffer, **obj)
            self.__set_buffer(target, res, buffer)
        return res

    def map(self, data):
        """Redirects data to new fields"""
        res = self.__execute__(data)
        return res

    __call__ = map
