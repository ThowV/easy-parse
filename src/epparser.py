from argument import Argument
from validator import validate


class Parser:
    registered_arguments: list[Argument] = []

    def add_arg(self, argument: Argument):
        self.registered_arguments.append(argument)

    def parse(self, input: str) -> dict:
        output: dict = {}
        parsed_input = input
        
        for argument in self.registered_arguments:
            result = validate(parsed_input, argument.atype)

            output[argument.name] = result[0]
            parsed_input = result[1]

        print(output)
        return output
