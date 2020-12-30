from typing import Union

from eptypes import EPType, instantiate


class Argument:
    name: str
    argument_type: EPType
    default: type
    dest: str

    def __init__(self, name: str, argument_type: Union[type, EPType], default: type = None, dest: str = ''):
        self.name = name
        self.argument_type = argument_type if isinstance(argument_type, EPType) else instantiate(argument_type)
        self.default = default
        self.dest = dest
