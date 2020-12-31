import unittest
from typing import Union

from epargument import Argument
from epparser import Parser
from eptypes import EPUnion


class TestParsingString(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.parser.clear_args()

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

    def test_union_standard_with_easy_parse_type(self):
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
