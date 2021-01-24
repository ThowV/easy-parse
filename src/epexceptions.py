from typing import Union


class EPException(Exception):
    pass


class ParsingFailedError(EPException):
    def __init__(self, value: str, to: Union[type, str], absolute: bool = False):
        self.value = value
        self.to = to.__name__ if not absolute else to

    def __str__(self) -> str:
        return f'Could not parse {self.value} to {self.to}.'


class ValidationFailedError(EPException):
    pass


# region Other
class ParsingStringFailedError(ParsingFailedError):
    def __init__(self, value: str):
        super().__init__(value, str)


class ParsingBoolFailedError(ParsingFailedError):
    def __init__(self, value: str):
        super().__init__(value, bool)


class ParsingUnionFailedError(ParsingFailedError):
    def __init__(self, value: str):
        super().__init__(value, 'union', True)
# endregion


# region Numerics
# region Numerics: ParsingNumericFailedError
class ParsingNumericFailedError(ParsingFailedError):
    def __init__(self, value: str, to: type = None):
        absolute = False if to else True
        to = to if to else 'numeric'
        super().__init__(value, to, absolute)


class ParsingIntFailedError(ParsingNumericFailedError):
    def __init__(self, value: str):
        super().__init__(value, int)


class ParsingFloatFailedError(ParsingNumericFailedError):
    def __init__(self, value: str):
        super().__init__(value, float)


class ParsingComplexFailedError(ParsingNumericFailedError):
    def __init__(self, value: str):
        super().__init__(value, complex)
# endregion


# region Numerics: NumericOverBoundError
class NumericOverBoundError(ValidationFailedError):
    def __init__(self, value: str, bound: str, direction: str = 'bound'):
        self.value = value
        self.bound = bound
        self.direction = direction

    def __str__(self) -> str:
        return f'The value {self.value} lies over the {self.direction} of {self.bound}.'


class NumericOverMinimumBoundError(NumericOverBoundError):
    def __init__(self, value: str, min: str):
        super().__init__(value, min, 'below')


class NumericOverMaximumBoundError(NumericOverBoundError):
    def __init__(self, value: str, max: str):
        super().__init__(value, max, 'above')


class IntOverMinimumBoundError(NumericOverMinimumBoundError):
    def __init__(self, value: int, min: int):
        super().__init__(str(value), str(min))


class IntOverMaximumBoundError(NumericOverMaximumBoundError):
    def __init__(self, value: int, max: int):
        super().__init__(str(value), str(max))


class FloatOverMinimumBoundError(NumericOverMinimumBoundError):
    def __init__(self, value: float, min: float):
        super().__init__(str(value), str(min))


class FloatOverMaximumBoundError(NumericOverMaximumBoundError):
    def __init__(self, value: float, max: float):
        super().__init__(str(value), str(max))
# endregion
# endregion


# region Collections
class ParsingCollectionFailedError(ParsingFailedError):
    def __init__(self, value: str, to: type = None):
        absolute = False if to else True
        to = to if to else 'collection'
        super().__init__(value, to, absolute)


class ParsingListFailedError(ParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, list)


class ParsingSetFailedError(ParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, set)


class ParsingFrozenSetFailedError(ParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, frozenset)


class ParsingTupleFailedError(ParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, tuple)


class ParsingDictFailedError(ParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, dict)


class ParsingRangeFailedError(ParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, range)
# endregion
