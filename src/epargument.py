from typing import Union, Callable

from eptypes import EPType, instantiate


class EPArgument:
    name: str
    argument_type: EPType
    default: type
    dest: str
    operation: Callable[[type], type]

    def __init__(self, name: str, argument_type: Union[type, EPType], default: type = None, dest: str = '',
                 operation: Callable[[type], type] = None):
        self.name = name
        self.argument_type = argument_type if isinstance(argument_type, EPType) else instantiate(argument_type)
        self.default = default
        self.dest = dest
        self.operation = operation
