from typing import Union, List, Set, FrozenSet, Tuple, Dict, get_origin, get_args


class Type:
    argument_type: type
    argument_sub_types: Union[tuple[any], None]

    def __init__(self, argument_type: type):
        self.argument_type = get_origin(argument_type) if get_origin(argument_type) else argument_type
        self.argument_sub_types = get_args(argument_type) if get_args(argument_type) else None


class Collection(Type):
    max_size: Union[int, None]

    def __init__(self,
                 argument_type: Union[list, List, set, Set, frozenset, FrozenSet, tuple, Tuple, dict, Dict, range],
                 max_size: int = None):
        super().__init__(argument_type)

        # Set the max size
        self.max_size = max_size

        if self.max_size:
            if self.argument_type == tuple and self.argument_sub_types:
                self.max_size *= len(self.argument_sub_types)
            elif self.argument_type == dict:
                self.max_size *= 2
            elif self.argument_type == range:
                self.max_size = 3  # Range has a fixed size of 3


def instantiate(argument_type: type) -> Type:
    argument_type_builtin = get_origin(argument_type) if get_origin(argument_type) else argument_type

    if argument_type_builtin in [list, set, frozenset, tuple, dict, range]:
        return Collection(argument_type)
    else:
        return Type(argument_type)
