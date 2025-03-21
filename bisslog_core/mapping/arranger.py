"""Implementation of the primitive data arranger"""
from datetime import datetime
from abc import ABC
from typing import Optional, Any


class IArranger(ABC):
    """Arranger interface in charge of processing primitive data by type

    Example
    -------
    arrangeData("420.4", dtype="number", defaultValue=100) -> 420.4
    arrangeData("", dtype="number", defaultValue=100) -> 100
    arrangeData("", dtype="number") -> None
    """
    def __init__(self):
        self.__processors = {
            # datetime
            "datetime": self.__processDatetime,
            "date": self.__processDatetime,
            # string
            "string": self.__processString,
            "str": self.__processString,
            # numbers
            "number": self.__processNumber,
            "float": self.__processNumber,
            "decimal": self.__processNumber,

            "integer": self.__processInteger,
            "int": self.__processInteger,

            # enum
            "enum": self.__processEnum,

            # no type
            "-": self.__processNotType
        }

    @staticmethod
    def __processDatetime(value, dateFormat="iso", defaultValue=None, transform=None, *_, **__):
        """Valid and formats if possible the value in a datetime as handled by events,
        otherwise returns None

        Parameters
        ----------
        value: object
            expected to be of type datetime

        Returns
        -------
        datetime: Object datetime
        """
        res = None
        if isinstance(value, datetime): res = value
        elif isinstance(value, (float, int)): res = datetime.fromtimestamp(value)
        elif isinstance(value, str):
            if dateFormat == "iso": res = datetime.fromisoformat(value)
            elif dateFormat == "timestamp" and value.replace(".", "", 1).isdigit():
                res = datetime.fromtimestamp(float(value))
            else:
                try: res = datetime.strptime(value, dateFormat)
                except ValueError: pass
        elif defaultValue == "now": res = datetime.now()


        if transform is not None and isinstance(res, datetime):
            if transform == "iso": res = res.isoformat()
            elif transform == "year": res = res.year
            elif transform == "day": res = res.day
            elif transform == "month": res = res.month
            elif transform == "weekday": res = res.weekday()
            elif transform == "hour": res = res.hour
            elif transform == "minute": res = res.minute
            elif transform == "timestamp": res = res.timestamp()
            elif transform == "time": res = res.time()
            elif transform == "date": res = res.date()
            elif transform == "fold": res = res.fold
        elif isinstance(res, datetime):
            res = res.timestamp()
        return res

    @staticmethod
    def __processEnum(value, enum, *_, **__):
        if value in enum: return value
        return None

    @staticmethod
    def __processString(value, *_, **__) -> str:
        """Valid and formats if possible the value in a string as handled by events,
        otherwise returns None

        Parameters
        ----------
        value: object
            expected to be of type string

        Returns
        -------
        str: Object string
        """
        return str(value)

    @staticmethod
    def __processInteger(value, *_, **__) -> Optional[int]:
        """Valid and formats if possible the value in an integer as handled by events,
        otherwise returns None

        Parameters
        ----------
        value: object
            expected to be of type integer

        Returns
        -------
        str, optional: Object integer
        """
        if isinstance(value, int): return value
        if (isinstance(value, str) and value.replace(".", "", 1).isdigit()) or \
                isinstance(value, bool):
            return int(value)
        return None

    @staticmethod
    def __processNumber(value, *_, **__) -> Optional[float]:
        """Valid and formats if possible the value in an integer as handled by events,
        otherwise returns None

        Parameters
        ----------
        value: object
            expected to be of type integer

        Returns
        -------
        str, optional: Object integer
        """
        if isinstance(value, (int, float)): return value
        if isinstance(value, str):
            if value.isdigit(): return int(value)
            if value.replace(".", "", 1).isdigit(): return float(value)
        return None

    @staticmethod
    def __processNotType(value, *_, **__):
        """Pass value

        Parameters
        ----------
        value: object

        Returns
        -------
        object, optional: Object integer
        """
        return value

    def arrangeValue(self, value, dtype: str= "-", defaultValue=None, *args, **kwargs) -> Any:
        """Organizes a value according to type and prevents it from remaining as a None.

        Parameters
        ----------
        value: object
            Value with primitive payload
        dtype: str, optional
            Valid data type
        defaultValue: object
            Default object to be imposed if it is set as None

        Returns
        -------
        object: Arranged value
        """
        if dtype in self.__processors and value is not None:
            _process = self.__processors[dtype]
            res = _process(value, defaultValue=defaultValue, *args, **kwargs)
            if res is not None:
                return res
        return defaultValue
