from arguments.argument import Argument
from typecheckers import boolean_checker, numeric_checker


class Parser:
    registered_arguments: list[Argument] = []

    def add_arg(self, argument: Argument):
        self.registered_arguments.append(argument)

    def parse(self, input: str) -> dict:
        output: dict = {}
        parsed_input = input
        
        for argument in self.registered_arguments:
            result = []
            #if argument.atype == str:
            #    parsed_input = string.check(parsed_input)
            if argument.atype == bool:
                result = boolean_checker.check(parsed_input)
            elif argument.atype == int:
                result = numeric_checker.check(parsed_input, int)
            elif argument.atype == float:
                result = numeric_checker.check(parsed_input, float)

            print(result)
            output[argument.name] = result[0]
            parsed_input = result[1]

        print(output)
        return output

    def x(self):
        pass
