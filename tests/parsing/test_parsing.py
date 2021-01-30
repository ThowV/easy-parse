import unittest

from epargument import EPArgument
from epexceptions import EPException, EPParsingFailedError, EPParsingOperationFailedError
from epparser import EPParser


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.parser = EPParser()
        self.parser.clear_args()

    def test_parsing_with_dest(self):
        # Assume
        assume = {'testDest': True}

        # Action
        self.parser.add_arg(EPArgument('a', dest='testDest', argument_type=bool))

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
    def test_parsing_operation_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int, operation=lambda x: x / 0))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '10')
        self.assertRaises(EPParsingFailedError, self.parser.parse, '10')
        self.assertRaises(EPParsingOperationFailedError, self.parser.parse, '10')
    # endregion
