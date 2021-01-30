from epexceptions import EPException, EPValidationFailedError, EPValueOverBoundError, EPCollectionOverBoundError, \
    EPFrozenSetOverBoundError, EPFrozenSetOverMinimumBoundError, EPFrozenSetOverMaximumBoundError
from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPFrozenSet


class TestParsingCollectionFrozenSet(TestParsing):
    def test_frozenset_standard(self):
        # Assume
        assume = {'a': {'a', '  trust', 'test', 'this is ', 'me'}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=frozenset))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_frozenset_easy_parse_type(self):
        # Assume
        assume = {'a': {'a', '  trust', 'test', 'this is ', 'me'}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPFrozenSet()))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_frozenset_standard_sub_typed(self):
        # Assume
        assume = {'a': {1, 2, 3}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=frozenset[int]))

        result = self.parser.parse('1 2 3')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_frozenset_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPFrozenSet(min_size=3)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPFrozenSetOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPFrozenSetOverMinimumBoundError, self.parser.parse, '1 2')

    def test_frozenset_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPFrozenSet(max_size=1)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPFrozenSetOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPFrozenSetOverMaximumBoundError, self.parser.parse, '1 2')
    # endregion
