import unittest

from epargument import Argument
from epparser import Parser
from eptypes import EPBool


class TestParsingString(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.parser.clear_args()

    def test_bool_standard(self):
        # Assume
        assume = {'a': True, 'b': False, 'c': True, 'd': False}

        # Action
        self.parser.add_arg(Argument('a', argument_type=bool))
        self.parser.add_arg(Argument('b', argument_type=bool))
        self.parser.add_arg(Argument('c', argument_type=bool))
        self.parser.add_arg(Argument('d', argument_type=bool))

        result = self.parser.parse('true false True False')

        # Assert
        self.assertEqual(assume, result)

    def test_bool_standard_with_easy_parse_type(self):
        # Assume
        assume = {'a': True, 'b': False, 'c': True, 'd': False}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPBool()))
        self.parser.add_arg(Argument('b', argument_type=EPBool()))
        self.parser.add_arg(Argument('c', argument_type=EPBool()))
        self.parser.add_arg(Argument('d', argument_type=EPBool()))

        result = self.parser.parse('true false True False')

        # Assert
        self.assertEqual(assume, result)

    def test_bool_numerics(self):
        # Assume
        assume = {'a': True, 'b': False, 'c': True, 'd': False}

        # Action
        self.parser.add_arg(Argument('a', argument_type=bool))
        self.parser.add_arg(Argument('b', argument_type=bool))
        self.parser.add_arg(Argument('c', argument_type=bool))
        self.parser.add_arg(Argument('d', argument_type=bool))

        result = self.parser.parse('1 0 "  1  " "  0  "')

        # Assert
        self.assertEqual(assume, result)
