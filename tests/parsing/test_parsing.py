import unittest

from epargument import EPArgument
from epexceptions import EPException, EPParsingFailedError, EPParsingOperationFailedError, EPParserSetupFailedError, \
    EPMandatoryArgumentInvalidPositionError, EPDuplicateArgumentError
from epparser import EPParser


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.parser = EPParser()
        self.parser.clear_args()

    def test_parsing_with_name(self):
        # Assume
        assume = {'a': True}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=bool))

        result = self.parser.parse('true')

        # Assert
        self.assertEqual(assume, result)

    def test_parsing_with_flags(self):
        # Assume
        assume = {'-f': True}

        # Action
        self.parser.add_arg(EPArgument('-f', '--flag', argument_type=bool))

        result = self.parser.parse('true')

        # Assert
        self.assertEqual(assume, result)

    def test_parsing_with_destination(self):
        # Assume
        assume = {'destination': True}

        # Action
        self.parser.add_arg(EPArgument('a', destination='destination', argument_type=bool))

        result = self.parser.parse('true')

        # Assert
        self.assertEqual(assume, result)

    def test_parsing_with_operation(self):
        # Assume
        assume = {'a': 10}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int, operation=lambda x: x * 2))

        result = self.parser.parse('5')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    # region Exceptions: EPParserSetupFailedError
    def test_duplicate_argument_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int))

        # Assert
        self.assertRaises(EPException, self.parser.add_arg, EPArgument('a', argument_type=int))
        self.assertRaises(EPParserSetupFailedError, self.parser.add_arg, EPArgument('a', argument_type=int))
        self.assertRaises(EPDuplicateArgumentError, self.parser.add_arg,
                          EPArgument('a', argument_type=int))

    def test_mandatory_argument_invalid_position_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int))
        self.parser.add_arg(EPArgument('b', argument_type=int))
        self.parser.add_arg(EPArgument('-c', argument_type=int))

        # Assert
        self.assertRaises(EPException, self.parser.add_arg, EPArgument('d', argument_type=int))
        self.assertRaises(EPParserSetupFailedError, self.parser.add_arg, EPArgument('d', argument_type=int))
        self.assertRaises(EPMandatoryArgumentInvalidPositionError, self.parser.add_arg,
                          EPArgument('d', argument_type=int))
    # endregion

    def test_parsing_operation_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int, operation=lambda x: x / 0))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '10')
        self.assertRaises(EPParsingFailedError, self.parser.parse, '10')
        self.assertRaises(EPParsingOperationFailedError, self.parser.parse, '10')
    # endregion
