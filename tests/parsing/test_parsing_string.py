from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPString


class TestParsingString(TestParsing):
    def test_string_no_quotes(self):
        # Assume
        assume = {'a': 'this', 'b': 'is', 'c': 'a', 'd': 'test', 'e': 'trust', 'f': 'me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))
        self.parser.add_arg(Argument('b', argument_type=str))
        self.parser.add_arg(Argument('c', argument_type=str))
        self.parser.add_arg(Argument('d', argument_type=str))
        self.parser.add_arg(Argument('e', argument_type=str))
        self.parser.add_arg(Argument('f', argument_type=str))

        result = self.parser.parse("this is a test trust me")

        # Assert
        self.assertEqual(assume, result)

    def test_string_no_quotes_with_easy_parse_type(self):
        # Assume
        assume = {'a': 'this', 'b': 'is', 'c': 'a', 'd': 'test', 'e': 'trust', 'f': 'me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPString()))
        self.parser.add_arg(Argument('b', argument_type=EPString()))
        self.parser.add_arg(Argument('c', argument_type=EPString()))
        self.parser.add_arg(Argument('d', argument_type=EPString()))
        self.parser.add_arg(Argument('e', argument_type=EPString()))
        self.parser.add_arg(Argument('f', argument_type=EPString()))

        result = self.parser.parse("this is a test trust me")

        # Assert
        self.assertEqual(assume, result)

    def test_string_single_quotes(self):
        # Assume
        assume = {'a': ' this is', 'b': 'a test ', 'c': ' trust me '}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))
        self.parser.add_arg(Argument('b', argument_type=str))
        self.parser.add_arg(Argument('c', argument_type=str))

        result = self.parser.parse("' this is' 'a test ' ' trust me '")

        # Assert
        self.assertEqual(assume, result)

    def test_string_double_quotes(self):
        # Assume
        assume = {'a': ' this is', 'b': 'a test ', 'c': ' trust me '}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))
        self.parser.add_arg(Argument('b', argument_type=str))
        self.parser.add_arg(Argument('c', argument_type=str))

        result = self.parser.parse('" this is" "a test " " trust me "')

        # Assert
        self.assertEqual(assume, result)

    def test_string_triple_quoted_using_single_quotes(self):
        # Assume
        assume = {'a': 'this \'is\' a "test" trust me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))

        result = self.parser.parse(""" '''this 'is' a "test" trust me''' """)

        # Assert
        self.assertEqual(assume, result)

    def test_string_triple_quoted_using_double_quotes(self):
        # Assume
        assume = {'a': 'this \'is\' a "test" trust me'}

        # Action
        self.parser.add_arg(Argument('a', argument_type=str))

        result = self.parser.parse(''' """this 'is' a "test" trust me""" ''')

        # Assert
        self.assertEqual(assume, result)
