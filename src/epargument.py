from typing import Union, Callable

from eptypes import EPType, instantiate


class EPArgument:
    identifiers: Union[tuple[str], str]
    argument_type: EPType
    default: type
    destination: str
    operation: Callable[[type], type]
    optional: bool

    def __init__(self, *identifiers: str, argument_type: Union[type, EPType], default: type = None,
                 destination: str = '', operation: Callable[[type], type] = None, optional: bool = None):
        # Determine and validate identifiers
        self.identifiers = identifiers

        # Determine destination
        if destination:
            self.destination = destination
        elif isinstance(identifiers, str):
            self.destination = identifiers
        else:
            self.destination = identifiers[0]

        # Determine optional
        if not optional:
            if self.identifiers[0].startswith('-'):
                self.optional = True
            else:
                self.optional = False
        else:
            self.optional = optional

        self.argument_type = argument_type if isinstance(argument_type, EPType) else instantiate(argument_type)
        self.default = default
        self.operation = operation
