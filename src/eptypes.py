from typing import Union, get_origin, get_args


class EPType:
    origin: type

    def __init__(self, argument_type: type):
        # Set the origin
        self.origin = get_origin(argument_type) if get_origin(argument_type) else argument_type


class EPTypeWithSub(EPType):
    sub_args: list

    def __init__(self, argument_type: type, sub_args: list = None):
        super().__init__(argument_type)

        # Set the sub arguments
        self.sub_args = sub_args if isinstance(sub_args, list) else ([sub_args] if sub_args else None)

        if not self.sub_args and get_args(argument_type):
            self.sub_args = list(get_args(argument_type))

        if self.sub_args:
            for index in range(len(self.sub_args)):
                # Make sure the type is not already an eptype
                if not isinstance(self.sub_args[index], EPType):
                    self.sub_args[index] = instantiate(self.sub_args[index])


# region Other
class EPString(EPType):
    def __init__(self):
        super().__init__(str)


class EPBool(EPType):
    def __init__(self):
        super().__init__(bool)


class EPUnion(EPTypeWithSub):
    def __init__(self, sub_args: list = None):
        super().__init__(Union[int, float], sub_args)
# endregion


# region Numeric
class EPNumeric(EPType):
    min: Union[int, float]
    max: Union[int, float]

    def __init__(self, argument_type: type, min: Union[int, float] = None, max: Union[int, float] = None):
        super().__init__(argument_type)

        self.min = min
        self.max = max


class EPInt(EPNumeric):
    def __init__(self, min: int = None, max: int = None):
        super().__init__(int, min=min, max=max)


class EPFloat(EPNumeric):
    def __init__(self, min: float = None, max: float = None):
        super().__init__(float, min=min, max=max)


class EPComplex(EPNumeric):
    def __init__(self):
        super().__init__(complex)
# endregion


# region Collection
class EPCollection(EPTypeWithSub):
    min_size: int
    max_size: int

    def __init__(self, argument_type: type, sub_args: list = None, min_size: int = None, max_size: int = None):
        super().__init__(argument_type, sub_args)

        if not self.sub_args:  # If there are no sub arguments provided
            self.sub_args = [instantiate(str)]

        self.min_size = min_size
        self.max_size = max_size


class EPList(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, min_size: int = None, max_size: int = None):
        super().__init__(list[str], sub_args, min_size, max_size)


class EPSet(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, min_size: int = None, max_size: int = None):
        super().__init__(set[str], sub_args, min_size, max_size)


class EPFrozenSet(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, min_size: int = None, max_size: int = None):
        super().__init__(frozenset[str], sub_args, min_size, max_size)


class EPTuple(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, min_size: int = None, max_size: int = None):
        super().__init__(tuple[str], sub_args, min_size, max_size)


class EPDict(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, min_size: int = None, max_size: int = None):
        super().__init__(dict[str, str], sub_args, min_size, max_size)


class EPRange(EPCollection):
    def __init__(self):
        super().__init__(range, sub_args=[int, int, int])
# endregion


def instantiate(argument_type: type) -> EPType:
    origin = get_origin(argument_type) if get_origin(argument_type) else argument_type
    sub_args = list(get_args(argument_type)) if get_args(argument_type) else None

    try:
        type_converting_dict = {
            # type :    [EPType,        Pass sub args]
            str:        [EPString,      False],

            bool:       [EPBool,        False],

            int:        [EPInt,         False],
            float:      [EPFloat,       False],
            complex:    [EPComplex,     False],

            Union:      [EPUnion,       True],

            list:       [EPList,        True],
            set:        [EPSet,         True],
            frozenset:  [EPFrozenSet,   True],
            tuple:      [EPTuple,       True],
            dict:       [EPDict,        True],
            range:      [EPRange,       False],
        }

        result = type_converting_dict[origin]

        if not result[1]:
            return result[0]()
        elif result[1]:
            return result[0](sub_args)
    except KeyError:
        return EPType(argument_type)
