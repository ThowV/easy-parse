from typing import Union


def check(input: str, atype: Union[int, float]):
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
