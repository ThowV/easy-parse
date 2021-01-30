from typing import Union


class EPException(Exception):
    pass


# region EPParsingFailedError
class EPParsingFailedError(EPException):
    def __init__(self, value: str, to: Union[type, str], absolute: bool = False):
        self.value = value
        self.to = to.__name__ if not absolute else to

    def __str__(self) -> str:
        return f'Could not parse {self.value} to {self.to}.'


class EPParsingOperationFailedError(EPParsingFailedError):
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return f'Could not perform operation on {self.value}.'


class EPParsingStringFailedError(EPParsingFailedError):
    def __init__(self, value: str):
        super().__init__(value, str)


class EPParsingBoolFailedError(EPParsingFailedError):
    def __init__(self, value: str):
        super().__init__(value, bool)


class EPParsingUnionFailedError(EPParsingFailedError):
    def __init__(self, value: str):
        super().__init__(value, 'union', True)


# region EPParsingFailedError -> EPParsingNumericFailedError
class EPParsingNumericFailedError(EPParsingFailedError):
    def __init__(self, value: str, to: type = None):
        absolute = False if to else True
        to = to if to else 'numeric'
        super().__init__(value, to, absolute)


class EPParsingIntFailedError(EPParsingNumericFailedError):
    def __init__(self, value: str):
        super().__init__(value, int)


class EPParsingFloatFailedError(EPParsingNumericFailedError):
    def __init__(self, value: str):
        super().__init__(value, float)


class EPParsingComplexFailedError(EPParsingNumericFailedError):
    def __init__(self, value: str):
        super().__init__(value, complex)
# endregion


# region EPParsingFailedError -> EPParsingCollectionFailedError
class EPParsingCollectionFailedError(EPParsingFailedError):
    def __init__(self, value: str, to: type = None):
        absolute = False if to else True
        to = to if to else 'collection'
        super().__init__(value, to, absolute)


class EPParsingListFailedError(EPParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, list)


class EPParsingSetFailedError(EPParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, set)


class EPParsingFrozenSetFailedError(EPParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, frozenset)


class EPParsingTupleFailedError(EPParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, tuple)


class EPParsingDictFailedError(EPParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, dict)


class EPParsingRangeFailedError(EPParsingCollectionFailedError):
    def __init__(self, value: str):
        super().__init__(value, range)
# endregion
# endregion


# region EPValidationFailedError
class EPValidationFailedError(EPException):
    pass


# region EPValidationFailedError -> EPValueOverBoundError
class EPValueOverBoundError(EPValidationFailedError):
    def __str__(self) -> str:
        return 'The given value surpassed one of the bounds.'


# region EPValidationFailedError -> EPValueOverBoundError -> EPNumericOverBoundError
class EPNumericOverBoundError(EPValueOverBoundError):
    def __init__(self, value: Union[int, float], bound: Union[int, float]):
        self.value = value
        self.bound = bound

    def __str__(self) -> str:
        return f'The value {self.value} lies {"over" if self.value > self.bound else "below"} the ' \
               f'{"maximum" if self.value > self.bound else "minimum"} of {self.bound}.'


# region EPValidationFailedError -> EPValueOverBoundError -> EPNumericOverBoundError -> EPIntOverBoundError
class EPIntOverBoundError(EPNumericOverBoundError):
    def __init__(self, value: int, bound: int):
        super().__init__(value, bound)


class EPIntOverMinimumBoundError(EPIntOverBoundError):
    def __init__(self, value: int, min: int):
        super().__init__(value, min)


class EPIntOverMaximumBoundError(EPIntOverBoundError):
    def __init__(self, value: int, max: int):
        super().__init__(value, max)
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPNumericOverBoundError -> EPFloatOverBoundError
class EPFloatOverBoundError(EPNumericOverBoundError):
    def __init__(self, value: float, bound: float):
        super().__init__(value, bound)


class EPFloatOverMinimumBoundError(EPFloatOverBoundError):
    def __init__(self, value: float, min: float):
        super().__init__(value, min)


class EPFloatOverMaximumBoundError(EPFloatOverBoundError):
    def __init__(self, value: float, max: float):
        super().__init__(value, max)
# endregion
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError
class EPCollectionOverBoundError(EPValueOverBoundError):
    def __init__(self, collection: Union[list, set, frozenset, tuple, dict, range], bound: int):
        self.collection = collection
        self.bound = bound

    def __str__(self) -> str:
        return f'The collection {self.collection} with a size of {len(self.collection)} ' \
               f'is too {"large" if len(self.collection) > self.bound == "above" else "small"} for the given ' \
               f'bound of {self.bound}.'


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError -> EPListOverBoundError
class EPListOverBoundError(EPCollectionOverBoundError):
    def __init__(self, collection: list, bound: int):
        super().__init__(collection, bound)


class EPListOverMinimumBoundError(EPListOverBoundError):
    def __init__(self, collection: list, min_size: int):
        super().__init__(collection, min_size)


class EPListOverMaximumBoundError(EPListOverBoundError):
    def __init__(self, collection: list, max_size: int):
        super().__init__(collection, max_size)
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError -> EPSetOverBoundError
class EPSetOverBoundError(EPCollectionOverBoundError):
    def __init__(self, collection: set, bound: int):
        super().__init__(collection, bound)


class EPSetOverMinimumBoundError(EPSetOverBoundError):
    def __init__(self, collection: set, min_size: int):
        super().__init__(collection, min_size)


class EPSetOverMaximumBoundError(EPSetOverBoundError):
    def __init__(self, collection: set, max_size: int):
        super().__init__(collection, max_size)
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError -> EPFrozenSetOverBoundError
class EPFrozenSetOverBoundError(EPCollectionOverBoundError):
    def __init__(self, collection: frozenset, bound: int):
        super().__init__(collection, bound)


class EPFrozenSetOverMinimumBoundError(EPFrozenSetOverBoundError):
    def __init__(self, collection: frozenset, min_size: int):
        super().__init__(collection, min_size)


class EPFrozenSetOverMaximumBoundError(EPFrozenSetOverBoundError):
    def __init__(self, collection: frozenset, max_size: int):
        super().__init__(collection, max_size)
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError -> EPTupleOverBoundError
class EPTupleOverBoundError(EPCollectionOverBoundError):
    def __init__(self, collection: tuple, bound: int):
        super().__init__(collection, bound)


class EPTupleOverMinimumBoundError(EPTupleOverBoundError):
    def __init__(self, collection: tuple, min_size: int):
        super().__init__(collection, min_size)


class EPTupleOverMaximumBoundError(EPTupleOverBoundError):
    def __init__(self, collection: tuple, max_size: int):
        super().__init__(collection, max_size)
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError -> EPDictOverBoundError
class EPDictOverBoundError(EPCollectionOverBoundError):
    def __init__(self, collection: dict, bound: int):
        super().__init__(collection, bound)


class EPDictOverMinimumBoundError(EPDictOverBoundError):
    def __init__(self, collection: dict, min_size: int):
        super().__init__(collection, min_size)


class EPDictOverMaximumBoundError(EPDictOverBoundError):
    def __init__(self, collection: dict, max_size: int):
        super().__init__(collection, max_size)
# endregion


# region EPValidationFailedError -> EPValueOverBoundError -> EPCollectionOverBoundError -> EPRangeOverBoundError
class EPRangeOverBoundError(EPCollectionOverBoundError):
    def __init__(self, collection: range, bound: int):
        super().__init__(collection, bound)


class EPRangeOverMinimumBoundError(EPRangeOverBoundError):
    def __init__(self, collection: range, min_size: int):
        super().__init__(collection, min_size)


class EPRangeOverMaximumBoundError(EPRangeOverBoundError):
    def __init__(self, collection: range, max_size: int):
        super().__init__(collection, max_size)
# endregion
# endregion
# endregion
# endregion
