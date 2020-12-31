import unittest

from epargument import Argument
from epparser import Parser
from eptypes import EPString


class TestParsingString(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.parser.clear_args()

    def test_string_no_quotes(self):
        # Assume
        assume = {'a': 'this', 'b': 'is', 'c': 'a', 'd': 'tests', 'e': 'trust', 'f': 'me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))
        self.parser.add_arg(Argument('b', argument_type=str))
        self.parser.add_arg(Argument('c', argument_type=str))
        self.parser.add_arg(Argument('d', argument_type=str))
        self.parser.add_arg(Argument('e', argument_type=str))
        self.parser.add_arg(Argument('f', argument_type=str))

        result = self.parser.parse("this is a tests trust me")

        # Assert
        self.assertEqual(assume, result)

    def test_string_no_quotes_with_easy_parse_type(self):
        # Assume
        assume = {'a': 'this', 'b': 'is', 'c': 'a', 'd': 'tests', 'e': 'trust', 'f': 'me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPString()))
        self.parser.add_arg(Argument('b', argument_type=EPString()))
        self.parser.add_arg(Argument('c', argument_type=EPString()))
        self.parser.add_arg(Argument('d', argument_type=EPString()))
        self.parser.add_arg(Argument('e', argument_type=EPString()))
        self.parser.add_arg(Argument('f', argument_type=EPString()))

        result = self.parser.parse("this is a tests trust me")

        # Assert
        self.assertEqual(assume, result)

    def test_string_single_quotes(self):
        # Assume
        assume = {'a': ' this is', 'b': 'a tests ', 'c': ' trust me '}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))
        self.parser.add_arg(Argument('b', argument_type=str))
        self.parser.add_arg(Argument('c', argument_type=str))

        result = self.parser.parse("' this is' 'a tests ' ' trust me '")

        # Assert
        self.assertEqual(assume, result)

    def test_string_double_quotes(self):
        # Assume
        assume = {'a': ' this is', 'b': 'a tests ', 'c': ' trust me '}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))
        self.parser.add_arg(Argument('b', argument_type=str))
        self.parser.add_arg(Argument('c', argument_type=str))

        result = self.parser.parse('" this is" "a tests " " trust me "')

        # Assert
        self.assertEqual(assume, result)

    def test_string_triple_quoted_using_single_quotes(self):
        # Assume
        assume = {'a': 'this \'is\' a "tests" trust me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))

        result = self.parser.parse(""" '''this 'is' a "tests" trust me''' """)

        # Assert
        self.assertEqual(assume, result)

    def test_string_triple_quoted_using_double_quotes(self):
        # Assume
        assume = {'a': 'this \'is\' a "tests" trust me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))

        result = self.parser.parse(''' """this 'is' a "tests" trust me""" ''')

        # Assert
        self.assertEqual(assume, result)
