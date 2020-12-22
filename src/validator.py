from typing import Union, get_args, get_origin, List


class StringValidateFinished(Exception): pass


def validate(input: str, atype: type) -> list:
    # Boolean
    if atype == bool:
        result = validate_boolean(input)
    # Numerics: Integer, float and complex
    elif atype == int or atype == float or atype == complex:
        result = validate_numeric(input, atype)
    # String
    elif atype == str:
        result = validate_string(input)
    # Union
    elif get_origin(atype) == Union:
        result = validate_union(input, atype)
    # List
    elif atype == list:
        result = validate_list(input)
    # List of type
    elif get_origin(atype) == list:
        result = validate_list(input, atype)
    else:
        result = ['', input]

    return result


def validate_boolean(input: str) -> list:
    input_split = input.split(' ', 1)

    if input_split[0].lower() == 'true':
        return [True, input_split[1] if len(input_split) > 1 else '']
    elif input_split[0].lower() == 'false':
        return [False, input_split[1] if len(input_split) > 1 else '']
    else:
        raise ValueError(f'Error parsing "{input}" since "{input_split[0]}" could not be parsed to a boolean.')


def validate_numeric(input: str, atype: Union[int, float, complex]) -> list:
    input_split = input.split(' ', 1)

    try:
        parsed_input: Union[int, float, complex] = 0

        if atype == int:
            parsed_input = int(input_split[0])
        elif atype == float:
            input_split[0] = input_split[0].replace(',', '.')  # Make sure the formatting is correct
            parsed_input = float(input_split[0])
        elif atype == complex:
            parsed_input = complex(input_split[0])

        return [parsed_input, input_split[1] if len(input_split) > 1 else '']
    except ValueError:
        raise ValueError(f'Error parsing "{input}" since "{input_split[0]}" could not be parsed to a numeric type.')


def validate_string(input: str) -> list:
    multi_word = False
    real_char_passed = False
    input_parsed = ''
    char_index = 0

    for index in range(len(input)):
        char_index = index
        input_parsed += input[index]

        # Check if we are looping through the first word and the character is a quotation mark
        if not multi_word and not real_char_passed and input[index] == '"':
            multi_word = True
        # Check if we are validating a multi word and the character is a quotation mark
        elif multi_word and real_char_passed and input[index] == '"':
            break

        # Check if we already passed anything else other than a space
        if input[index] != ' ':
            real_char_passed = True

        # Check if we are entering a second word whilst multi word is not active
        if real_char_passed and not multi_word and input[index] == ' ':
            break

    # Remove useless white space
    input_parsed = input_parsed.strip()

    # Remove the quotation marks
    if multi_word:
        input_parsed = input_parsed[1:len(input_parsed) - 1]

    return [input_parsed, input[char_index + 1:]]


def validate_union(input: str, atype: Union) -> list:
    for sub_atype in get_args(atype):
        try:
            parsed_input = validate(input, sub_atype)
            return parsed_input
        except ValueError:
            continue

    return ['', input]


def validate_list(input: str, atype=List[str]) -> list:
    unparsed_input = input
    parsed_input = []
    sub_type = get_args(atype)[0]

    while len(unparsed_input) > 0:
        parsed = validate_string(unparsed_input)
        parsed_input.append(parsed[0])
        unparsed_input = parsed[1] if len(parsed) > 1 else ''

    # Check if the sub type is not string, this is the default, no need to parse twice
    if sub_type != str:
        for index in range(len(parsed_input)):
            parsed_input[index] = validate(parsed_input[index], sub_type)[0]

    return [parsed_input, unparsed_input[1] if unparsed_input else '']
