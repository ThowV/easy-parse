from typing import Union, get_args, get_origin


def validate(input: str, atype: type) -> list:
    if atype == bool:
        result = validate_boolean(input)
    elif atype == int:
        result = validate_numeric(input, int)
    elif atype == float:
        result = validate_numeric(input, float)
    elif get_origin(atype) == Union:
        result = validate_union(input, atype)
    else:
        result = ['', input]

    return result


def validate_boolean(input: str) -> list:
    input_split = input.split(' ', 1)

    if input_split[0].lower() == 'true':
        return [True, input_split[1]]
    elif input_split[0].lower() == 'false':
        return [False, input_split[1]]
    else:
        raise ValueError(f'Error parsing "{input}" since "{input_split[0]}" could not be parsed to a boolean.')


def validate_numeric(input: str, atype: Union[int, float]) -> list:
    input_split = input.split(' ', 1)

    try:
        parsed_input: Union[int, float] = 0

        if atype == int:
            parsed_input = int(input_split[0])
        elif atype == float:
            input_split[0] = input_split[0].replace(',', '.')  # Make sure the formatting is correct
            parsed_input = float(input_split[0])

        return [parsed_input, input_split[1] if len(input_split) > 1 else '']
    except ValueError:
        raise ValueError(f'Error parsing "{input}" since "{input_split[0]}" could not be parsed to a numeric type.')


def validate_union(input: str, atype: Union) -> list:
    # input_split = input.split(' ', 1)
    print(get_args(atype))

    for sub_atype in get_args(atype):
        try:
            parsed_input = validate(input, sub_atype)
            return parsed_input
        except ValueError:
            continue

    return ['', input]
