from typing import Tuple

from epexceptions import EPException, EPValidationFailedError, EPValueOverBoundError, EPCollectionOverBoundError, \
    EPTupleOverBoundError, EPTupleOverMinimumBoundError, EPTupleOverMaximumBoundError
from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPTuple


class TestParsingCollectionTuple(TestParsing):
    def test_tuple_standard(self):
        # Assume
        assume = {'a': ('string1', 2, 3.3, True, 'string4', 5, 6.6, True)}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=Tuple[str, int, float, bool]))

        result = self.parser.parse('string1 2 3.3 true string4 5 6.6 true')

        # Assert
        self.assertEqual(assume, result)

    def test_tuple_easy_parse_type(self):
        # Assume
        assume = {'a': ('string1', '2', '3.3', 'true', 'string4', '5', '6.6', 'true')}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPTuple()))

        result = self.parser.parse('string1 2 3.3 true string4 5 6.6 true')

        # Assert
        self.assertEqual(assume, result)

    def test_tuple_standard_sub_typed(self):
        # Assume
        assume = {'a': ('string1', 2, 3.3, True, 'string4', 5, 6.6, True)}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=tuple[str, int, float, bool]))

        result = self.parser.parse('string1 2 3.3 true string4 5 6.6 true')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_tuple_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPTuple(min_size=3)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPTupleOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPTupleOverMinimumBoundError, self.parser.parse, '1 2')

    def test_tuple_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPTuple(max_size=1)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1 2')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1 2')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPTupleOverBoundError, self.parser.parse, '1 2')
        self.assertRaises(EPTupleOverMaximumBoundError, self.parser.parse, '1 2')
    # endregion
