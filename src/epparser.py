from argument import Argument
from enum import Enum
from typing import Union, get_args, get_origin


class Parser:
    registered_arguments: list[Argument] = []

    def add_arg(self, argument: Argument):
        self.registered_arguments.append(argument)

    def clear_args(self):
        self.registered_arguments = []

    def parse(self, input: str) -> dict:
        output: dict = {}
        parsed_input = input
        
        for argument in self.registered_arguments:
            result = parse(parsed_input, argument.atype)

            output[argument.name] = result[0]
            parsed_input = result[1]

        return output


class StringType(Enum):
    STANDARD = 0
    SINGLE = 1
    DOUBLE = 2
    TRIPLE_SINGLE = 3
    TRIPLE_DOUBLE = 4


def string_to_string_type(string: str) -> StringType:
    if string == "'":
        return StringType.SINGLE
    elif string == '"':
        return StringType.DOUBLE
    elif string == "'''":
        return StringType.TRIPLE_SINGLE
    elif string == '"""':
        return StringType.TRIPLE_DOUBLE
    else:
        return StringType.STANDARD


def parse(input: str, atype: type) -> list:
    atype_original = atype
    atype = get_origin(atype) if get_origin(atype) else atype

    # Boolean
    if atype == bool:
        result = parse_boolean(input)
    # Numerics: Integer, float and complex
    elif atype == int or atype == float or atype == complex:
        result = parse_numeric(input, atype_original)
    # String
    elif atype == str:
        result = parse_string(input)
    # Union
    elif atype == Union:
        result = parse_union(input, atype_original)
    # List, set, tuple, dictionary or range
    elif atype == list or atype == set or atype == frozenset or atype == tuple or atype == dict or atype == range:
        result = parse_collection(input, atype_original)
    else:
        result = ['', input]

    return result


def parse_string(input: str) -> list:
    string_type = None
    string_type_start = ''
    string_type_stop = ''
    input = input.strip()
    index_top = 0

    for index in range(len(input)):
        index_top = index + 1

        # When we have a string type, check if we reached the end
        if string_type:
            if string_type != StringType.STANDARD:
                if input[index] in string_type_start:
                    # We might have reached the end
                    string_type_stop += input[index]  # Add to the string type stop value for the next iteration
                else:
                    # This is not the end so reset the string type stop value
                    string_type_stop = ''

                # Check if we have reached the end by checking the string type stop value
                if string_to_string_type(string_type_stop) == string_type:
                    break
            elif string_type == StringType.STANDARD and input[index] == ' ':
                break

        # Figure out what type of string we are dealing with
        if not string_type:
            # If the string starts out with a quote we must check how many quotes of what type there are
            # in order to get the actual type
            if input[index] in ["'", '"']:
                string_type_start += input[index]
                index_next = (index + 1) if (index + 1) < len(input) else None

                # If the string type is not STANDARD or the next character is
                # the same as the current we have to check the type further
                if index_next and input[index_next] != input[index]:
                    string_type = string_to_string_type(string_type_start.strip())
            # If the string starts with anything other than a quote it must be of STANDARD type
            else:
                string_type = StringType.STANDARD

    # Finalization
    output = input[len(string_type_start):(index_top - len(string_type_stop))]
    input_left = input[len(string_type_start) + index_top:]

    if string_type == StringType.STANDARD:
        output = output.strip()

    return [output, input_left]


def parse_boolean(input: str) -> list:
    input_as_string = parse_string(input)

    if input_as_string[0].lower().strip() == 'true' or input_as_string[0].strip() == '1':
        return [True, input_as_string[1] if len(input_as_string) > 1 else '']
    elif input_as_string[0].lower().strip() == 'false' or input_as_string[0].strip() == '0':
        return [False, input_as_string[1] if len(input_as_string) > 1 else '']
    else:
        raise ValueError(f'Error parsing "{input}" since "{input_as_string[0]}" could not be parsed to a boolean.')


def parse_numeric(input: str, atype: Union[int, float, complex]) -> list:
    input_as_string = parse_string(input)

    try:
        parsed_input: Union[int, float, complex] = 0

        if atype == int:
            parsed_input = int(input_as_string[0])
        elif atype == float:
            input_as_string[0] = input_as_string[0].replace(',', '.')  # Make sure the formatting is correct
            parsed_input = float(input_as_string[0])
        elif atype == complex:
            parsed_input = complex(input_as_string[0])

        return [parsed_input, input_as_string[1] if len(input_as_string) > 1 else '']
    except ValueError:
        raise ValueError(f'Error parsing "{input}" since "{input_as_string[0]}" could not be parsed to a numeric type.')


def parse_union(input: str, atype: Union) -> list:
    for sub_atype in get_args(atype):
        try:
            return parse(input, sub_atype)
        except ValueError:
            continue

    return ['', input]


def parse_collection(input: str, atype: Union[list, set, frozenset, tuple, dict, range]) -> list:
    input_unparsed = input
    output = []

    # Parse everything to string first
    while len(input_unparsed) > 0:
        parsed = parse_string(input_unparsed)
        output.append(parsed[0])
        input_unparsed = parsed[1] if len(parsed) > 1 else ''

    # Parse all the subtypes
    sub_types = get_args(atype) if get_args(atype) else [str]

    if atype == range:
        sub_types = [int, int, int]

    for index in range(len(output)):
        sub_type_index = index % len(sub_types)

        # Check if the sub type is not string, this is the default, no need to parse twice
        if sub_types[sub_type_index] != str:
            output[index] = parse(output[index], sub_types[sub_type_index])[0]

    # Transform the list into whatever type was provided
    if atype == set or get_origin(atype) == set:
        output = set(output)
    elif atype == frozenset or get_origin(atype) == frozenset:
        output = frozenset(output)
    elif atype == tuple or get_origin(atype) == tuple:
        output = tuple(output)
    elif atype == dict or get_origin(atype) == dict:
        output = {output[i]: output[i + 1] for i in range(0, len(output), 2)}
    elif atype == range:
        output = range(*output)

    return [output, input_unparsed[1] if input_unparsed else '']
