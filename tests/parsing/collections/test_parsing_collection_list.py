from epexceptions import EPException, EPValidationFailedError, EPValueOverBoundError, EPCollectionOverBoundError, \
    EPListOverBoundError, EPListOverMinimumBoundError, EPListOverMaximumBoundError
from tests.parsing.test_parsing import TestParsing

from epargument import EPArgument
from eptypes import EPList


class TestParsingCollectionList(TestParsing):
    def test_list_standard(self):
        # Assume
        assume = {'a': ['this is ', 'a', 'test', '  trust', 'me']}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=list))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_list_easy_parse_type(self):
        # Assume
        assume = {'a': ['this is ', 'a', 'test', '  trust', 'me']}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPList()))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_list_standard_sub_typed(self):
        # Assume
        assume = {'a': [1, 2, 3]}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=list[int]))

        result = self.parser.parse('1 2 3')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_list_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPList(min_size=3)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPListOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPListOverMinimumBoundError, self.parser.parse, '1 2')

    def test_list_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPList(max_size=1)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPListOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPListOverMaximumBoundError, self.parser.parse, '1 2')
    # endregion
