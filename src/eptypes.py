from typing import Union, get_origin, get_args


class EPType:
    origin: type

    def __init__(self, argument_type: type):
        # Set the origin
        self.origin = get_origin(argument_type) if get_origin(argument_type) else argument_type


# region Inherits EPType
class EPString(EPType):
    def __init__(self):
        super().__init__(str)


class EPBool(EPType):
    def __init__(self):
        super().__init__(bool)


class EPNumeric(EPType):
    def __init__(self, argument_type: type):
        super().__init__(argument_type)


# region Inherits EPNumeric
class EPInt(EPNumeric):
    def __init__(self):
        super().__init__(int)


class EPFloat(EPNumeric):
    def __init__(self):
        super().__init__(float)


class EPComplex(EPNumeric):
    def __init__(self):
        super().__init__(complex)
# endregion
# endregion


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


# region Inherits EPTypeWithSub
class EPUnion(EPTypeWithSub):
    def __init__(self, sub_args: list = None):
        super().__init__(Union[int, float], sub_args)


class EPCollection(EPTypeWithSub):
    max_size: int

    def __init__(self, argument_type: type, sub_args: list = None, max_size: int = None):
        super().__init__(argument_type, sub_args)

        if not self.sub_args:  # If there are no sub arguments provided
            self.sub_args = [instantiate(str)]

        self.max_size = max_size


# region Inherits EPCollection
class EPList(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, max_size: int = None):
        super().__init__(list[str], sub_args, max_size)


class EPSet(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, max_size: int = None):
        super().__init__(set[str], sub_args, max_size)


class EPFrozenSet(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, max_size: int = None):
        super().__init__(frozenset[str], sub_args, max_size)


class EPTuple(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, max_size: int = None):
        if sub_args and max_size:
            max_size *= len(sub_args)

        super().__init__(tuple[str], sub_args, max_size)


class EPDict(EPCollection):
    def __init__(self, sub_args: Union[type, list] = None, max_size: int = None):
        if max_size:
            max_size *= 2

        super().__init__(dict[str, str], sub_args, max_size)


class EPRange(EPCollection):
    def __init__(self):
        super().__init__(range, sub_args=[int, int, int], max_size=3)
# endregion
# endregion


def instantiate(argument_type: type) -> EPType:
    origin = get_origin(argument_type) if get_origin(argument_type) else argument_type
    sub_args = list(get_args(argument_type)) if get_args(argument_type) else None

    try:
        type_converting_dict = {
            # type :    [EPType, Pass sub args]
            str:        [EPString, False],

            bool:       [EPBool, False],

            int:        [EPInt, False],
            float:      [EPFloat, False],
            complex:    [EPComplex, False],

            Union: [EPUnion, True],

            list:       [EPList, True],
            set:        [EPSet, True],
            frozenset:  [EPFrozenSet, True],
            tuple:      [EPTuple, True],
            dict:       [EPDict, True],
            range:      [EPRange, False],
        }

        result = type_converting_dict[origin]

        if not result[1]:
            return result[0]()
        elif result[1]:
            return result[0](sub_args)
    except KeyError:
        return EPType(argument_type)
