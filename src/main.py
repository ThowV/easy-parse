import pprint

from typing import Union
from argument import Argument
from epparser import Parser

if __name__ == '__main__':
    parser = Parser()

    # Booleans
    parser.add_arg(Argument('a', atype=bool))
    parser.add_arg(Argument('b', atype=bool))
    pprint.pprint(parser.parse('true false'))
    print('-------------------------------')
    parser.clear_args()

    # Numerics
    parser.add_arg(Argument('a', atype=int))
    parser.add_arg(Argument('b', atype=float))
    parser.add_arg(Argument('c', atype=float))
    parser.add_arg(Argument('d', atype=complex))
    pprint.pprint(parser.parse('1 2.2 3,3 4+4j'))
    print('-------------------------------')
    parser.clear_args()

    # Unions
    parser.add_arg(Argument('a', atype=Union[int, float]))
    parser.add_arg(Argument('b', atype=Union[int, float]))
    parser.add_arg(Argument('c', atype=Union[float, int]))
    parser.add_arg(Argument('d', atype=Union[float, int]))
    parser.add_arg(Argument('e', atype=Union[Union[int, float], int]))
    pprint.pprint(parser.parse('1 2.2 3,3 4 5.5'))
    print('-------------------------------')
    parser.clear_args()

    # Strings
    parser.add_arg(Argument('a', atype=str))
    parser.add_arg(Argument('b', atype=str))
    parser.add_arg(Argument('c', atype=str))
    parser.add_arg(Argument('d', atype=str))
    pprint.pprint(parser.parse('this is "a test" "trust me"'))
    print('-------------------------------')
    parser.clear_args()

    # Intricate strings
    parser.add_arg(Argument('a', atype=str))
    parser.add_arg(Argument('b', atype=str))
    parser.add_arg(Argument('c', atype=str))
    parser.add_arg(Argument('d', atype=str))
    pprint.pprint(parser.parse('"this is " a test "  trust"'))
    print('-------------------------------')
    parser.clear_args()
