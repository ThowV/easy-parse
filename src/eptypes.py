from typing import Union, List, Set, FrozenSet, Tuple, Dict, get_origin, get_args


class Type:
    origin: type
    sub_args: Union[list, None]

    def __init__(self, argument_type: type):
        # Set the origin
        self.origin = get_origin(argument_type) if get_origin(argument_type) else argument_type

        # Set the sub arguments
        if get_args(argument_type):
            self.sub_args = list(get_args(argument_type))

            for index in range(len(self.sub_args)):
                # Make sure the type is not already an eptype
                if not isinstance(self.sub_args[index], Type):
                    self.sub_args[index] = instantiate(self.sub_args[index])
        else:
            self.sub_args = None


class Collection(Type):
    max_size: Union[int, None]

    def __init__(self,
                 argument_type: Union[list, List, set, Set, frozenset, FrozenSet, tuple, Tuple, dict, Dict, range],
                 max_size: int = None):
        super().__init__(argument_type)

        # Set the sub argument type
        if self.origin == range:  # If the origin is range we always set the sub types manually
            self.sub_args = [instantiate(int_type) for int_type in [int, int, int]]
        elif not self.sub_args:  # If there are no sub types provided and the origin is not range
            self.sub_args = [instantiate(str)]

        # Set the max size
        self.max_size = max_size

        if self.max_size:
            if self.origin == tuple and self.sub_args:
                self.max_size *= len(self.sub_args)
            elif self.origin == dict:
                self.max_size *= 2
            elif self.origin == range:
                self.max_size = 3  # Range has a fixed size of 3


def instantiate(argument_type: type) -> Type:
    argument_type_builtin = get_origin(argument_type) if get_origin(argument_type) else argument_type

    if argument_type_builtin in [list, set, frozenset, tuple, dict, range]:
        return Collection(argument_type)
    else:
        return Type(argument_type)
