from epexceptions import NumericOverMinimumBoundError, IntOverMinimumBoundError, FloatOverMinimumBoundError, \
    NumericOverMaximumBoundError, IntOverMaximumBoundError, FloatOverMaximumBoundError, ParsingNumericFailedError, \
    ParsingIntFailedError, ParsingFloatFailedError, ParsingComplexFailedError, NumericOverBoundError, \
    ValidationFailedError, EPException
from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPInt, EPFloat, EPComplex


class TestParsingNumeric(TestParsing):
    def test_numeric_standard(self):
        # Assume
        assume = {'a': 1, 'b': 2.2, 'c': 3.3, 'd': (4+4j), 'e': 5.5}

        # Action
        self.parser.add_arg(Argument('a', argument_type=int))
        self.parser.add_arg(Argument('b', argument_type=float))
        self.parser.add_arg(Argument('c', argument_type=float))
        self.parser.add_arg(Argument('d', argument_type=complex))
        self.parser.add_arg(Argument('e', argument_type=float))

        result = self.parser.parse('1 2.2 3,3 4+4j "   5.5  "')

        # Assert
        self.assertEqual(assume, result)

    def test_numeric_easy_parse_type(self):
        # Assume
        assume = {'a': 1, 'b': 2.2, 'c': 3.3, 'd': (4+4j), 'e': 5.5}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPInt()))
        self.parser.add_arg(Argument('b', argument_type=EPFloat()))
        self.parser.add_arg(Argument('c', argument_type=EPFloat()))
        self.parser.add_arg(Argument('d', argument_type=EPComplex()))
        self.parser.add_arg(Argument('e', argument_type=EPFloat()))

        result = self.parser.parse('1 2.2 3,3 4+4j "   5.5  "')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    # region Exceptions: ParsingNumericFailedError
    def test_int_parsing_failed_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=int))

        # Assert
        self.assertRaises(ParsingNumericFailedError, self.parser.parse, 'x')
        self.assertRaises(ParsingIntFailedError, self.parser.parse, 'x')

    def test_float_parsing_failed_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=float))

        # Assert
        self.assertRaises(ParsingNumericFailedError, self.parser.parse, 'x')
        self.assertRaises(ParsingFloatFailedError, self.parser.parse, 'x')

    def test_complex_parsing_failed_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=complex))

        # Assert
        self.assertRaises(ParsingNumericFailedError, self.parser.parse, 'x')
        self.assertRaises(ParsingComplexFailedError, self.parser.parse, 'x')
    # endregion

    # region Exceptions: NumericOverBoundError
    # region Exceptions: NumericOverBoundError -> NumericOverMinimumBoundError
    def test_int_standard_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=EPInt(min=10)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1')
        self.assertRaises(ValidationFailedError, self.parser.parse, '1')
        self.assertRaises(NumericOverBoundError, self.parser.parse, '1')
        self.assertRaises(NumericOverMinimumBoundError, self.parser.parse, '1')
        self.assertRaises(IntOverMinimumBoundError, self.parser.parse, '1')

    def test_float_standard_over_minimum_bound_error(self):
        # Action
        self.parser.clear_args()
        self.parser.add_arg(Argument('a', argument_type=EPFloat(min=10)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1.1')
        self.assertRaises(ValidationFailedError, self.parser.parse, '1.1')
        self.assertRaises(NumericOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(NumericOverMinimumBoundError, self.parser.parse, '1.1')
        self.assertRaises(FloatOverMinimumBoundError, self.parser.parse, '1.1')
    # endregion

    # region Exceptions: NumericOverBoundError -> NumericOverMaximumError
    def test_int_standard_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=EPInt(max=0)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1')
        self.assertRaises(ValidationFailedError, self.parser.parse, '1')
        self.assertRaises(NumericOverBoundError, self.parser.parse, '1')
        self.assertRaises(NumericOverMaximumBoundError, self.parser.parse, '1')
        self.assertRaises(IntOverMaximumBoundError, self.parser.parse, '1')

    def test_float_standard_over_maximum_bound_error(self):
        # Action
        self.parser.clear_args()
        self.parser.add_arg(Argument('a', argument_type=EPFloat(max=0)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1.1')
        self.assertRaises(ValidationFailedError, self.parser.parse, '1.1')
        self.assertRaises(NumericOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(NumericOverMaximumBoundError, self.parser.parse, '1.1')
        self.assertRaises(FloatOverMaximumBoundError, self.parser.parse, '1.1')
    # endregion
    # endregion
