def check(input: str):
    input_split = input.split(' ', 1)

    if input_split[0].lower() == 'true':
        return [True, input_split[1]]
    elif input_split[0].lower() == 'false':
        return [False, input_split[1]]
    else:
        raise ValueError(f'Error parsing "{input}" since "{input_split[0]}" could not be parsed to a boolean.')
