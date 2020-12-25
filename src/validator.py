from enum import Enum
from typing import Union, get_args, get_origin


class StringType(Enum):
    STANDARD = 0
    SINGLE = 1
    DOUBLE = 2
    TRIPLE_SINGLE = 3
    TRIPLE_DOUBLE = 4


def string_to_type(string: str) -> StringType:
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


def validate(input: str, atype: type) -> list:
    atype_original = atype
    atype = get_origin(atype) if get_origin(atype) else atype

    # Boolean
    if atype == bool:
        result = validate_boolean(input)
    # Numerics: Integer, float and complex
    elif atype == int or atype == float or atype == complex:
        result = validate_numeric(input, atype_original)
    # String
    elif atype == str:
        result = validate_string(input)
    # Union
    elif atype == Union:
        result = validate_union(input, atype_original)
    # List, set, tuple, dictionary or range
    elif atype == list or atype == set or atype == frozenset or atype == tuple or atype == dict or atype == range:
        result = validate_collection(input, atype_original)
    else:
        result = ['', input]

    return result


def validate_boolean(input: str) -> list:
    input_parsed = validate_string(input)

    if input_parsed[0].lower().strip() == 'true' or input_parsed[0].strip() == '1':
        return [True, input_parsed[1] if len(input_parsed) > 1 else '']
    elif input_parsed[0].lower().strip() == 'false' or input_parsed[0].strip() == '0':
        return [False, input_parsed[1] if len(input_parsed) > 1 else '']
    else:
        raise ValueError(f'Error parsing "{input}" since "{input_parsed[0]}" could not be parsed to a boolean.')


def validate_numeric(input: str, atype: Union[int, float, complex]) -> list:
    parsed_string = validate_string(input)

    try:
        parsed_input: Union[int, float, complex] = 0

        if atype == int:
            parsed_input = int(parsed_string[0])
        elif atype == float:
            parsed_string[0] = parsed_string[0].replace(',', '.')  # Make sure the formatting is correct
            parsed_input = float(parsed_string[0])
        elif atype == complex:
            parsed_input = complex(parsed_string[0])

        return [parsed_input, parsed_string[1] if len(parsed_string) > 1 else '']
    except ValueError:
        raise ValueError(f'Error parsing "{input}" since "{parsed_string[0]}" could not be parsed to a numeric type.')


def validate_string(input: str) -> list:
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
                if string_to_type(string_type_stop) == string_type:
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
                    string_type = string_to_type(string_type_start.strip())
            # If the string starts with anything other than a quote it must be of STANDARD type
            else:
                string_type = StringType.STANDARD

    # Finalization
    output = input[len(string_type_start):(index_top - len(string_type_stop))]
    input_left = input[len(string_type_start) + index_top:]

    if string_type == StringType.STANDARD:
        output = output.strip()

    return [output, input_left]


def validate_union(input: str, atype: Union) -> list:
    for sub_atype in get_args(atype):
        try:
            parsed_input = validate(input, sub_atype)
            return parsed_input
        except ValueError:
            continue

    return ['', input]


def validate_collection(input: str, atype: Union[list, set, frozenset, tuple, dict, range]) -> list:
    unparsed_input = input
    parsed_input = []

    # Parse everything to string first
    while len(unparsed_input) > 0:
        parsed = validate_string(unparsed_input)
        parsed_input.append(parsed[0])
        unparsed_input = parsed[1] if len(parsed) > 1 else ''

    # Parse all the subtypes
    sub_types = get_args(atype) if get_args(atype) else [str]

    if atype == range:
        sub_types = [int, int, int]

    for index in range(len(parsed_input)):
        sub_type_index = index % len(sub_types)

        # Check if the sub type is not string, this is the default, no need to parse twice
        if sub_types[sub_type_index] != str:
            parsed_input[index] = validate(parsed_input[index], sub_types[sub_type_index])[0]

    # Transform the list into whatever type was provided
    if atype == set or get_origin(atype) == set:
        parsed_input = set(parsed_input)
    elif atype == frozenset or get_origin(atype) == frozenset:
        parsed_input = frozenset(parsed_input)
    elif atype == tuple or get_origin(atype) == tuple:
        parsed_input = tuple(parsed_input)
    elif atype == dict or get_origin(atype) == dict:
        parsed_input = {parsed_input[i]: parsed_input[i + 1] for i in range(0, len(parsed_input), 2)}
    elif atype == range:
        parsed_input = range(*parsed_input)

    return [parsed_input, unparsed_input[1] if unparsed_input else '']
