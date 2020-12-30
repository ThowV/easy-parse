import pprint

from typing import Union, List, Tuple
from epargument import Argument
from epparser import Parser
from eptypes import Collection

if __name__ == '__main__':
    parser = Parser()

    print('\n------------Booleans------------')
    parser.add_arg(Argument('a', argument_type=bool))
    parser.add_arg(Argument('b', argument_type=bool))
    parser.add_arg(Argument('c', argument_type=bool))
    parser.add_arg(Argument('d', argument_type=bool))
    parser.add_arg(Argument('e', argument_type=bool))
    parser.add_arg(Argument('f', argument_type=bool))
    parser.add_arg(Argument('g', argument_type=bool))
    pprint.pprint(parser.parse('true false False 1 0 "  1  " "  0  "'))
    parser.clear_args()

    print('\n------------Numerics------------')
    parser.add_arg(Argument('a', argument_type=int))
    parser.add_arg(Argument('b', argument_type=float))
    parser.add_arg(Argument('c', argument_type=float))
    parser.add_arg(Argument('d', argument_type=complex))
    parser.add_arg(Argument('e', argument_type=float))
    pprint.pprint(parser.parse('1 2.2 3,3 4+4j "   5.5  "'))
    parser.clear_args()

    print('\n------------Unions------------')
    parser.add_arg(Argument('a', argument_type=Union[int, float]))
    parser.add_arg(Argument('b', argument_type=Union[int, float]))
    parser.add_arg(Argument('c', argument_type=Union[float, int]))
    parser.add_arg(Argument('d', argument_type=Union[float, int]))
    parser.add_arg(Argument('e', argument_type=Union[Union[int, float], int]))
    pprint.pprint(parser.parse('1 2.2 3,3 4 5.5'))
    parser.clear_args()

    print('\n------------Strings: No quotes------------')
    parser.add_arg(Argument('a', argument_type=str))
    parser.add_arg(Argument('b', argument_type=str))
    parser.add_arg(Argument('c', argument_type=str))
    parser.add_arg(Argument('d', argument_type=str))
    parser.add_arg(Argument('e', argument_type=str))
    parser.add_arg(Argument('f', argument_type=str))
    pprint.pprint(parser.parse("this is a test trust me"))
    parser.clear_args()

    print('------------Strings: Single quotes------------')
    parser.add_arg(Argument('a', argument_type=str))
    parser.add_arg(Argument('b', argument_type=str))
    parser.add_arg(Argument('c', argument_type=str))
    pprint.pprint(parser.parse("' this is' 'a test ' ' trust me '"))
    parser.clear_args()

    print('------------Strings: Double quotes------------')
    parser.add_arg(Argument('a', argument_type=str))
    parser.add_arg(Argument('b', argument_type=str))
    parser.add_arg(Argument('c', argument_type=str))
    pprint.pprint(parser.parse('" this is" "a test " " trust me "'))
    parser.clear_args()

    print('------------Strings: Triple quoted using single quotes------------')
    parser.add_arg(Argument('a', argument_type=str))
    pprint.pprint(parser.parse(""" '''this 'is' a "test" trust me''' """))
    parser.clear_args()

    print('------------Strings: Triple quoted using double quotes------------')
    parser.add_arg(Argument('a', argument_type=str))
    pprint.pprint(parser.parse(''' """this 'is' a "test" trust me""" '''))
    parser.clear_args()

    print('\n------------Lists------------')
    parser.add_arg(Argument('a', argument_type=list))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('------------Lists: Easy parser type------------')
    parser.add_arg(Argument('a', argument_type=Collection(list, max_size=3)))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('------------Lists: Sub types------------')
    parser.add_arg(Argument('a', argument_type=List[int]))
    pprint.pprint(parser.parse('1 2 3'))
    parser.clear_args()

    print('------------Lists: Union as sub type------------')
    parser.add_arg(Argument('a', argument_type=List[Union[int, float]]))
    pprint.pprint(parser.parse('1 2.2 3,3'))
    parser.clear_args()

    print('------------Lists: Nested easy parser types------------')
    parser.add_arg(Argument('a', argument_type=Collection(list[Collection(list, max_size=2)], max_size=3)))
    pprint.pprint(parser.parse('the ultimate test trust me for once in your life'))
    parser.clear_args()

    print('\n------------Sets------------')
    parser.add_arg(Argument('a', argument_type=set))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('\n------------Frozen sets------------')
    parser.add_arg(Argument('a', argument_type=frozenset))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('\n------------Tuples------------')
    parser.add_arg(Argument('a', argument_type=Tuple[str, int, float, bool]))
    pprint.pprint(parser.parse('string1 2 3.3 true string4 5 6.6 true'))
    parser.clear_args()

    print('------------Tuples: Easy parser type------------')
    print(Tuple[str, int, float, bool])
    parser.add_arg(Argument('a', argument_type=Collection(Tuple[str, int, float, bool], max_size=1)))
    pprint.pprint(parser.parse('string1 2 3.3 true string4 5 6.6 true'))
    parser.clear_args()

    print('\n------------Dictionaries------------')
    parser.add_arg(Argument('a', argument_type=dict[str, int]))
    pprint.pprint(parser.parse('key1 2 key3 4 key5 6'))
    parser.clear_args()

    print('------------Dictionaries: Easy parser type------------')
    parser.add_arg(Argument('a', argument_type=Collection(dict[str, int], 2)))
    pprint.pprint(parser.parse('key1 2 key3 4 key5 6'))
    parser.clear_args()

    print('\n------------Ranges------------')
    parser.add_arg(Argument('a', argument_type=range))
    pprint.pprint(parser.parse('0 20 2'))
    parser.clear_args()
