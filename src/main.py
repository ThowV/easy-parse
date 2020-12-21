from arguments.argument import Argument
from epparser import Parser

if __name__ == '__main__':
    parser = Parser()

    parser.add_arg(Argument('a', atype=bool))
    parser.add_arg(Argument('b', atype=bool))
    parser.add_arg(Argument('c', atype=int))
    parser.add_arg(Argument('d', atype=float))
    parser.add_arg(Argument('e', atype=float))
    parser.add_arg(Argument('f', atype=int))

    parser.parse('true False 101011 1000.1 10001,1 69')
