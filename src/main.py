import pprint

from typing import Union, List, Tuple
from epargument import Argument
from epparser import Parser
from eptypes import EPCollection, EPList, EPDict, EPRange, EPSet, EPFrozenSet, EPTuple, EPBool

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

    print('\n------------Booleans: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPList(EPBool())))
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

    print('------------Lists: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPCollection(list, max_size=3)))
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

    print('------------Lists: Nested easy parse types------------')
    parser.add_arg(Argument('a', argument_type=EPList(sub_args=[EPList(max_size=2)], max_size=3)))
    pprint.pprint(parser.parse('the ultimate test trust me for once in your life'))
    parser.clear_args()

    print('\n------------Sets------------')
    parser.add_arg(Argument('a', argument_type=set))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('------------Sets: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPSet()))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('\n------------Frozen sets------------')
    parser.add_arg(Argument('a', argument_type=frozenset))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('------------Frozen: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPFrozenSet()))
    pprint.pprint(parser.parse('"this is " a test "  trust" me'))
    parser.clear_args()

    print('\n------------Tuples------------')
    parser.add_arg(Argument('a', argument_type=Tuple[str, int, float, bool]))
    pprint.pprint(parser.parse('string1 2 3.3 true string4 5 6.6 true'))
    parser.clear_args()

    print('------------Tuples: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPTuple(sub_args=[str, int, float, bool], max_size=1)))
    pprint.pprint(parser.parse('string1 2 3.3 true string4 5 6.6 true'))
    parser.clear_args()

    print('\n------------Dictionaries------------')
    parser.add_arg(Argument('a', argument_type=dict[str, int]))
    pprint.pprint(parser.parse('key1 2 key3 4 key5 6'))
    parser.clear_args()

    print('------------Dictionaries: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPDict(sub_args=[str, int], max_size=2)))
    pprint.pprint(parser.parse('key1 2 key3 4 key5 6'))
    parser.clear_args()

    print('\n------------Ranges------------')
    parser.add_arg(Argument('a', argument_type=range))
    pprint.pprint(parser.parse('0 20 2'))
    parser.clear_args()

    print('------------Ranges: Easy parse type------------')
    parser.add_arg(Argument('a', argument_type=EPRange()))
    pprint.pprint(parser.parse('1 5'))
    parser.clear_args()
