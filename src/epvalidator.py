from typing import Union

from epexceptions import IntOverMinimumBoundError, IntOverMaximumBoundError, FloatOverMinimumBoundError, FloatOverMaximumBoundError
from eptypes import EPNumeric


def validate_numeric(argument_type: EPNumeric, parsed_input: Union[int, float, complex]):
    # Check minimum and maximum
    if argument_type.min is not None and parsed_input < argument_type.min:
        if isinstance(parsed_input, int):
            raise IntOverMinimumBoundError(parsed_input, argument_type.min)
        elif isinstance(parsed_input, float):
            raise FloatOverMinimumBoundError(parsed_input, argument_type.min)

    if argument_type.max is not None and parsed_input > argument_type.max:
        if isinstance(parsed_input, int):
            raise IntOverMaximumBoundError(parsed_input, argument_type.max)
        elif isinstance(parsed_input, float):
            raise FloatOverMaximumBoundError(parsed_input, argument_type.max)
