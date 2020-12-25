from typing import Union

from eptypes import Type


class Argument:
    name: str
    argument_type: Union[type, Type]
    default: type
    dest: str

    def __init__(self, name: str, argument_type: Union[type, Type], default: type = None, dest: str = ''):
        self.name = name
        self.argument_type = argument_type
        self.default = default
        self.dest = dest
