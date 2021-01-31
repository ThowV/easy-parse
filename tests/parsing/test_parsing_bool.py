from epexceptions import EPParsingFailedError, EPParseToBoolFailedError, EPException, EPParseToTypeFailedError
from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPBool


class TestParsingBool(TestParsing):
    def test_bool_standard(self):
        # Assume
        assume = {'a': True, 'b': False, 'c': True, 'd': False}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=bool))
        self.parser.add_arg(EPArgument('b', argument_type=bool))
        self.parser.add_arg(EPArgument('c', argument_type=bool))
        self.parser.add_arg(EPArgument('d', argument_type=bool))

        result = self.parser.parse('true false True False')

        # Assert
        self.assertEqual(assume, result)

    def test_bool_easy_parse_type(self):
        # Assume
        assume = {'a': True, 'b': False, 'c': True, 'd': False}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPBool()))
        self.parser.add_arg(EPArgument('b', argument_type=EPBool()))
        self.parser.add_arg(EPArgument('c', argument_type=EPBool()))
        self.parser.add_arg(EPArgument('d', argument_type=EPBool()))

        result = self.parser.parse('true false True False')

        # Assert
        self.assertEqual(assume, result)

    def test_bool_standard_numerics(self):
        # Assume
        assume = {'a': True, 'b': False, 'c': True, 'd': False}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=bool))
        self.parser.add_arg(EPArgument('b', argument_type=bool))
        self.parser.add_arg(EPArgument('c', argument_type=bool))
        self.parser.add_arg(EPArgument('d', argument_type=bool))

        result = self.parser.parse('1 0 "  1  " "  0  "')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_parse_to_bool_failed_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=bool))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'x')
        self.assertRaises(EPParsingFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToTypeFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToBoolFailedError, self.parser.parse, 'x')
    # endregion
