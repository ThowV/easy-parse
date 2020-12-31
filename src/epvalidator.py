from typing import Union

from epexceptions import IntUnderMinimumError, IntOverMaximumError, FloatUnderMinimumError, FloatOverMaximumError
from eptypes import EPNumeric


def validate_numeric(argument_type: EPNumeric, numeric: Union[int, float, complex]):
    # Check minimum and maximum
    if isinstance(argument_type.min, int) and numeric < argument_type.min:
        if isinstance(numeric, int):
            raise IntUnderMinimumError
        elif isinstance(numeric, float):
            raise FloatUnderMinimumError

    if isinstance(argument_type.max, int) and numeric > argument_type.max:
        if isinstance(numeric, int):
            raise IntOverMaximumError
        elif isinstance(numeric, float):
            raise FloatOverMaximumError
