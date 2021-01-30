from typing import Union

from epexceptions import EPIntOverMinimumBoundError, EPIntOverMaximumBoundError, EPFloatOverMinimumBoundError, \
    EPFloatOverMaximumBoundError, EPListOverMaximumBoundError, EPSetOverMaximumBoundError, \
    EPFrozenSetOverMaximumBoundError, EPTupleOverMaximumBoundError, EPDictOverMaximumBoundError, \
    EPRangeOverMaximumBoundError, EPListOverMinimumBoundError, EPFrozenSetOverMinimumBoundError, \
    EPSetOverMinimumBoundError, EPTupleOverMinimumBoundError, EPDictOverMinimumBoundError, EPRangeOverMinimumBoundError
from eptypes import EPNumeric, EPCollection


def validate_numeric(argument_type: EPNumeric, input: Union[int, float, complex]):
    # Check minimum
    if argument_type.min is not None and input < argument_type.min:
        if isinstance(input, int):
            raise EPIntOverMinimumBoundError(input, argument_type.min)
        elif isinstance(input, float):
            raise EPFloatOverMinimumBoundError(input, argument_type.min)

    # Check maximum
    if argument_type.max is not None and input > argument_type.max:
        if isinstance(input, int):
            raise EPIntOverMaximumBoundError(input, argument_type.max)
        elif isinstance(input, float):
            raise EPFloatOverMaximumBoundError(input, argument_type.max)


def validate_collection(argument_type: EPCollection, input: Union[list, set, frozenset, tuple, dict, range]):
    # Check minimum
    if argument_type.min_size is not None and len(input) < argument_type.min_size:
        if isinstance(input, list):
            raise EPListOverMinimumBoundError(input, argument_type.min_size)
        elif isinstance(input, set):
            raise EPSetOverMinimumBoundError(input, argument_type.min_size)
        elif isinstance(input, frozenset):
            raise EPFrozenSetOverMinimumBoundError(input, argument_type.min_size)
        elif isinstance(input, tuple):
            raise EPTupleOverMinimumBoundError(input, argument_type.min_size)
        elif isinstance(input, dict):
            raise EPDictOverMinimumBoundError(input, argument_type.min_size)
        elif isinstance(input, range):
            raise EPRangeOverMinimumBoundError(input, argument_type.min_size)

    # Check maximum
    if argument_type.max_size is not None and len(input) > argument_type.max_size:
        if isinstance(input, list):
            raise EPListOverMaximumBoundError(input, argument_type.max_size)
        elif isinstance(input, set):
            raise EPSetOverMaximumBoundError(input, argument_type.max_size)
        elif isinstance(input, frozenset):
            raise EPFrozenSetOverMaximumBoundError(input, argument_type.max_size)
        elif isinstance(input, tuple):
            raise EPTupleOverMaximumBoundError(input, argument_type.max_size)
        elif isinstance(input, dict):
            raise EPDictOverMaximumBoundError(input, argument_type.max_size)
        elif isinstance(input, range):
            raise EPRangeOverMaximumBoundError(input, argument_type.max_size)
