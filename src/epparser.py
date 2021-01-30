from epargument import EPArgument
from enum import Enum
from typing import Union

from epexceptions import EPParsingBoolFailedError, EPParsingNumericFailedError, EPParsingIntFailedError, \
    EPParsingFloatFailedError, EPParsingComplexFailedError, EPParsingFailedError, EPParsingUnionFailedError, \
    EPParsingCollectionFailedError, EPParsingSetFailedError, EPParsingFrozenSetFailedError, EPParsingTupleFailedError, \
    EPParsingDictFailedError, EPParsingRangeFailedError
from eptypes import EPType, EPCollection, EPTypeWithSub, EPNumeric
from epvalidator import validate_numeric, validate_collection


class EPParser:
    registered_arguments: list[EPArgument] = []

    def add_arg(self, argument: EPArgument):
        self.registered_arguments.append(argument)

    def clear_args(self):
        self.registered_arguments = []

    def parse(self, input: str) -> dict:
        output: dict = {}
        parsed_input = input
        
        for argument in self.registered_arguments:
            result = parse(parsed_input, argument.argument_type)

            output[argument.dest if argument.dest else argument.name] = result[0]
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


def parse(input: str, argument_type: EPType) -> list:
    if argument_type.origin == bool:
        result = parse_boolean(input)
    elif argument_type.origin in [int, float, complex]:
        result = parse_numeric(input, argument_type)
    elif argument_type.origin == str:
        result = parse_string(input)
    elif argument_type.origin == Union:
        result = parse_union(input, argument_type)
    elif isinstance(argument_type, EPCollection):
        result = parse_collection(input, argument_type)
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
    input = parse_string(input)

    if input[0].lower().strip() == 'true' or input[0].strip() == '1':
        return [True, input[1] if len(input) > 1 else '']
    elif input[0].lower().strip() == 'false' or input[0].strip() == '0':
        return [False, input[1] if len(input) > 1 else '']
    else:
        raise EPParsingBoolFailedError(input[0])


def parse_numeric(input: str, argument_type: EPNumeric) -> list:
    input = parse_string(input)
    exception = EPParsingNumericFailedError

    try:
        parsed_input: Union[int, float, complex] = 0

        if argument_type.origin == int:
            exception = EPParsingIntFailedError
            parsed_input = int(input[0])
        elif argument_type.origin == float:
            exception = EPParsingFloatFailedError
            input[0] = input[0].replace(',', '.')  # Make sure the formatting is correct
            parsed_input = float(input[0])
        elif argument_type.origin == complex:
            exception = EPParsingComplexFailedError
            parsed_input = complex(input[0])
    except ValueError:
        raise exception(input[0])

    # Validate the numeric
    validate_numeric(argument_type, parsed_input)

    return [parsed_input, input[1] if len(input) > 1 else '']


def parse_union(input: str, argument_type: EPTypeWithSub) -> list:
    for sub_atype in argument_type.sub_args:
        try:
            return parse(input, sub_atype)
        except EPParsingFailedError:
            continue

    raise EPParsingUnionFailedError(input)


def parse_collection(input: str, argument_type: EPCollection) -> list:
    input_unparsed = input
    output = []
    exception = EPParsingCollectionFailedError

    # Parse all the sub arguments
    sub_args = argument_type.sub_args

    for index in range(len(input_unparsed)):
        sub_arg_index = index % len(sub_args)

        parsed = parse(input_unparsed, sub_args[sub_arg_index])

        output.append(parsed[0])
        input_unparsed = parsed[1] if len(parsed) > 1 else ''

        # Check if the input is empty
        if not input_unparsed:
            break

    # Transform the list into whatever type was provided
    try:
        if argument_type.origin == set:
            exception = EPParsingSetFailedError
            output = set(output)
        elif argument_type.origin == frozenset:
            exception = EPParsingFrozenSetFailedError
            output = frozenset(output)
        elif argument_type.origin == tuple:
            exception = EPParsingTupleFailedError
            output = tuple(output)
        elif argument_type.origin == dict:
            exception = EPParsingDictFailedError
            output = {output[i]: output[i + 1] for i in range(0, len(output), 2)}
        elif argument_type.origin == range:
            exception = EPParsingRangeFailedError
            output = range(*output)
    except ValueError or IndexError or TypeError:
        raise exception(str(output))

    # Validate the collection
    validate_collection(argument_type, output)

    return [output, input_unparsed if input_unparsed else '']
