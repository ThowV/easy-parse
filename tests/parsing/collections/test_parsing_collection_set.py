from epexceptions import EPException, EPValidationFailedError, EPValueOverBoundError, EPCollectionOverBoundError, \
    EPSetOverBoundError, EPSetOverMinimumBoundError, EPSetOverMaximumBoundError
from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPSet


class TestParsingCollectionSet(TestParsing):
    def test_set_standard(self):
        # Assume
        assume = {'a': {'a', '  trust', 'test', 'this is ', 'me'}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=set))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_set_easy_parse_type(self):
        # Assume
        assume = {'a': {'test', 'this is ', '  trust', 'me', 'a'}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPSet()))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_set_standard_sub_typed(self):
        # Assume
        assume = {'a': {1, 2, 3}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=set[int]))

        result = self.parser.parse('1 2 3')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_set_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPSet(min_size=3)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPSetOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPSetOverMinimumBoundError, self.parser.parse, '1 2')

    def test_set_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPSet(max_size=1)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPSetOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPSetOverMaximumBoundError, self.parser.parse, '1 2')
    # endregion
