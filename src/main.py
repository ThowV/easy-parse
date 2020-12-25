import pprint

from typing import Union, List, Tuple
from argument import Argument
from epparser import Parser

if __name__ == '__main__':
    parser = Parser()

    print('\n------------Booleans------------')
    parser.add_arg(Argument('a', atype=bool))
    parser.add_arg(Argument('b', atype=bool))
    parser.add_arg(Argument('c', atype=bool))
    parser.add_arg(Argument('d', atype=bool))
    parser.add_arg(Argument('e', atype=bool))
    parser.add_arg(Argument('f', atype=bool))
    parser.add_arg(Argument('g', atype=bool))
    pprint.pprint(parser.parse('true false False 1 0 "  1  " "  0  "'))
    parser.clear_args()

    print('\n------------Numerics------------')
    parser.add_arg(Argument('a', atype=int))
    parser.add_arg(Argument('b', atype=float))
    parser.add_arg(Argument('c', atype=float))
    parser.add_arg(Argument('d', atype=complex))
    parser.add_arg(Argument('e', atype=float))
    pprint.pprint(parser.parse('1 2.2 3,3 4+4j "   5.5  "'))
    parser.clear_args()

    print('\n------------Unions------------')
    parser.add_arg(Argument('a', atype=Union[int, float]))
    parser.add_arg(Argument('b', atype=Union[int, float]))
    parser.add_arg(Argument('c', atype=Union[float, int]))
    parser.add_arg(Argument('d', atype=Union[float, int]))
    parser.add_arg(Argument('e', atype=Union[Union[int, float], int]))
    pprint.pprint(parser.parse('1 2.2 3,3 4 5.5'))
    parser.clear_args()

    print('\n------------Strings: No quotes------------')
    parser.add_arg(Argument('a', atype=str))
    parser.add_arg(Argument('b', atype=str))
    parser.add_arg(Argument('c', atype=str))
    parser.add_arg(Argument('d', atype=str))
    parser.add_arg(Argument('e', atype=str))
    parser.add_arg(Argument('f', atype=str))
    pprint.pprint(parser.parse("this is a test trust me"))
    parser.clear_args()

    print('------------Strings: Single quotes------------')
    parser.add_arg(Argument('a', atype=str))
    parser.add_arg(Argument('b', atype=str))
    parser.add_arg(Argument('c', atype=str))
    pprint.pprint(parser.parse("' this is' 'a test ' ' trust me '"))
    parser.clear_args()

    print('------------Strings: Double quotes------------')
    parser.add_arg(Argument('a', atype=str))
    parser.add_arg(Argument('b', atype=str))
    parser.add_arg(Argument('c', atype=str))
    pprint.pprint(parser.parse('" this is" "a test " " trust me "'))
    parser.clear_args()

    print('------------Strings: Triple quoted using single quotes------------')
    parser.add_arg(Argument('a', atype=str))
    pprint.pprint(parser.parse(""" '''this 'is' a "test" trust me''' """))
    parser.clear_args()

    print('------------Strings: Triple quoted using double quotes------------')
    parser.add_arg(Argument('a', atype=str))
    pprint.pprint(parser.parse(''' """this 'is' a "test" trust me""" '''))
    parser.clear_args()

    print('\n------------Lists------------')
    parser.add_arg(Argument('a', atype=list))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('------------Lists: Sub types------------')
    parser.add_arg(Argument('a', atype=List[int]))
    pprint.pprint(parser.parse('1 2 3'))
    parser.clear_args()

    print('------------Lists: Union as sub type------------')
    parser.add_arg(Argument('a', atype=List[Union[int, float]]))
    pprint.pprint(parser.parse('1 2.2 3,3'))
    parser.clear_args()

    print('\n------------Sets------------')
    parser.add_arg(Argument('a', atype=set))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('\n------------Frozen sets------------')
    parser.add_arg(Argument('a', atype=frozenset))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('\n------------Tuples------------')
    parser.add_arg(Argument('a', atype=Tuple[str, int, float, bool]))
    pprint.pprint(parser.parse('string1 2 3.3 true string4 5 6.6 true'))
    parser.clear_args()

    print('\n------------Dictionaries------------')
    parser.add_arg(Argument('a', atype=dict[str, int]))
    pprint.pprint(parser.parse('key1 2 key3 4 key5 6'))
    parser.clear_args()

    print('\n------------Ranges------------')
    parser.add_arg(Argument('a', atype=range))
    pprint.pprint(parser.parse('0 20 2'))
    parser.clear_args()
