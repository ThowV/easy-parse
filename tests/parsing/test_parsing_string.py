from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPString


class TestParsingString(TestParsing):
    def test_string_standard_no_quotes(self):
        # Assume
        assume = {'a': 'this', 'b': 'is', 'c': 'a', 'd': 'test', 'e': 'trust', 'f': 'me'}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=str))
        self.parser.add_arg(EPArgument('b', argument_type=str))
        self.parser.add_arg(EPArgument('c', argument_type=str))
        self.parser.add_arg(EPArgument('d', argument_type=str))
        self.parser.add_arg(EPArgument('e', argument_type=str))
        self.parser.add_arg(EPArgument('f', argument_type=str))

        result = self.parser.parse("this is a test trust me")

        # Assert
        self.assertEqual(assume, result)

    def test_string_easy_parse_type_no_quotes(self):
        # Assume
        assume = {'a': 'this', 'b': 'is', 'c': 'a', 'd': 'test', 'e': 'trust', 'f': 'me'}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPString()))
        self.parser.add_arg(EPArgument('b', argument_type=EPString()))
        self.parser.add_arg(EPArgument('c', argument_type=EPString()))
        self.parser.add_arg(EPArgument('d', argument_type=EPString()))
        self.parser.add_arg(EPArgument('e', argument_type=EPString()))
        self.parser.add_arg(EPArgument('f', argument_type=EPString()))

        result = self.parser.parse("this is a test trust me")

        # Assert
        self.assertEqual(assume, result)

    def test_string_standard_single_quotes(self):
        # Assume
        assume = {'a': ' this is', 'b': 'a test ', 'c': ' trust me '}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=str))
        self.parser.add_arg(EPArgument('b', argument_type=str))
        self.parser.add_arg(EPArgument('c', argument_type=str))

        result = self.parser.parse("' this is' 'a test ' ' trust me '")

        # Assert
        self.assertEqual(assume, result)

    def test_string_standard_double_quotes(self):
        # Assume
        assume = {'a': ' this is', 'b': 'a test ', 'c': ' trust me '}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=str))
        self.parser.add_arg(EPArgument('b', argument_type=str))
        self.parser.add_arg(EPArgument('c', argument_type=str))

        result = self.parser.parse('" this is" "a test " " trust me "')

        # Assert
        self.assertEqual(assume, result)

    def test_string_standard_triple_quoted_using_single_quotes(self):
        # Assume
        assume = {'a': 'this \'is\' a "test" trust me'}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=str))

        result = self.parser.parse(""" '''this 'is' a "test" trust me''' """)

        # Assert
        self.assertEqual(assume, result)

    def test_string_standard_triple_quoted_using_double_quotes(self):
        # Assume
        assume = {'a': 'this \'is\' a "test" trust me'}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=str))

        result = self.parser.parse(''' """this 'is' a "test" trust me""" ''')

        # Assert
        self.assertEqual(assume, result)
