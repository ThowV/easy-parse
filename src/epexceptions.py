class NumericUnderMinimumError(Exception):
    pass


class IntUnderMinimumError(NumericUnderMinimumError):
    pass


class FloatUnderMinimumError(NumericUnderMinimumError):
    pass


class NumericOverMaximumError(Exception):
    pass


class IntOverMaximumError(NumericOverMaximumError):
    pass


class FloatOverMaximumError(NumericOverMaximumError):
    pass

