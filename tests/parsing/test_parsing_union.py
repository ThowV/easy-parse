from typing import Union

from epexceptions import ParsingFailedError, ParsingUnionFailedError, EPException
from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPUnion


class TestParsingUnion(TestParsing):
    def test_union_standard(self):
        # Assume
        assume = {'a': 1, 'b': 2.2, 'c': 3.3, 'd': 4.0}

        # Action
        self.parser.add_arg(Argument('a', argument_type=Union[int, float]))
        self.parser.add_arg(Argument('b', argument_type=Union[int, float]))
        self.parser.add_arg(Argument('c', argument_type=Union[float, int]))
        self.parser.add_arg(Argument('d', argument_type=Union[float, int]))

        result = self.parser.parse('1 2.2 3,3 4')

        # Assert
        self.assertEqual(assume, result)

    def test_union_easy_parse_type(self):
        # Assume
        assume = {'a': 1, 'b': 2.2, 'c': 3.3, 'd': 4.0}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPUnion([int, float])))
        self.parser.add_arg(Argument('b', argument_type=EPUnion([int, float])))
        self.parser.add_arg(Argument('c', argument_type=EPUnion([float, int])))
        self.parser.add_arg(Argument('d', argument_type=EPUnion([float, int])))

        result = self.parser.parse('1 2.2 3,3 4')

        # Assert
        self.assertEqual(assume, result)

    def test_union_standard_nested(self):
        # Assume
        assume = {'a': 1.1}

        # Action
        self.parser.add_arg(Argument('a', argument_type=Union[Union[int, complex], float]))

        result = self.parser.parse('1.1')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_union_standard_parsing_failed_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=Union[int, complex]))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'x')
        self.assertRaises(ParsingFailedError, self.parser.parse, 'x')
        self.assertRaises(ParsingUnionFailedError, self.parser.parse, 'x')
    # endregion
