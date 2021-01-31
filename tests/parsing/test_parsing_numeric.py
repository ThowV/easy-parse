from epexceptions import EPIntOverMinimumBoundError, EPFloatOverMinimumBoundError, \
    EPIntOverMaximumBoundError, EPFloatOverMaximumBoundError, EPParseToNumericFailedError, \
    EPParseToIntFailedError, EPParseToFloatFailedError, EPParseToComplexFailedError, EPNumericOverBoundError, \
    EPValidationFailedError, EPException, EPValueOverBoundError, EPIntOverBoundError, EPFloatOverBoundError, \
    EPParsingFailedError, EPParseToTypeFailedError
from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPInt, EPFloat, EPComplex


class TestParsingNumeric(TestParsing):
    def test_numeric_standard(self):
        # Assume
        assume = {'a': 1, 'b': 2.2, 'c': 3.3, 'd': (4+4j), 'e': 5.5}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int))
        self.parser.add_arg(EPArgument('b', argument_type=float))
        self.parser.add_arg(EPArgument('c', argument_type=float))
        self.parser.add_arg(EPArgument('d', argument_type=complex))
        self.parser.add_arg(EPArgument('e', argument_type=float))

        result = self.parser.parse('1 2.2 3,3 4+4j "   5.5  "')

        # Assert
        self.assertEqual(assume, result)

    def test_numeric_easy_parse_type(self):
        # Assume
        assume = {'a': 1, 'b': 2.2, 'c': 3.3, 'd': (4+4j), 'e': 5.5}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPInt()))
        self.parser.add_arg(EPArgument('b', argument_type=EPFloat()))
        self.parser.add_arg(EPArgument('c', argument_type=EPFloat()))
        self.parser.add_arg(EPArgument('d', argument_type=EPComplex()))
        self.parser.add_arg(EPArgument('e', argument_type=EPFloat()))

        result = self.parser.parse('1 2.2 3,3 4+4j "   5.5  "')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    # region Exceptions: EPParseToNumericFailedError
    def test_parse_to_int_failed_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=int))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'x')
        self.assertRaises(EPParsingFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToTypeFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToNumericFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToIntFailedError, self.parser.parse, 'x')

    def test_parse_to_float_failed_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=float))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'x')
        self.assertRaises(EPParsingFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToTypeFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToNumericFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToFloatFailedError, self.parser.parse, 'x')

    def test_parse_to_complex_failed_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=complex))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'x')
        self.assertRaises(EPParsingFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToTypeFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToNumericFailedError, self.parser.parse, 'x')
        self.assertRaises(EPParseToComplexFailedError, self.parser.parse, 'x')
    # endregion

    # region Exceptions: EPNumericOverBoundError
    # region Exceptions: EPNumericOverBoundError -> NumericOverMinimumBoundError
    def test_int_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPInt(min=10)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPNumericOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPIntOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPIntOverMinimumBoundError, self.parser.parse, '1')

    def test_float_over_minimum_bound_error(self):
        # Action
        self.parser.clear_args()
        self.parser.add_arg(EPArgument('a', argument_type=EPFloat(min=10)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1.1')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1.1')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(EPNumericOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(EPFloatOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(EPFloatOverMinimumBoundError, self.parser.parse, '1.1')
    # endregion

    # region Exceptions: EPNumericOverBoundError -> NumericOverMaximumError
    def test_int_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPInt(max=0)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPNumericOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPIntOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPIntOverMaximumBoundError, self.parser.parse, '1')

    def test_float_over_maximum_bound_error(self):
        # Action
        self.parser.clear_args()
        self.parser.add_arg(EPArgument('a', argument_type=EPFloat(max=0)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, '1.1')
        self.assertRaises(EPValidationFailedError, self.parser.parse, '1.1')
        self.assertRaises(EPNumericOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, '1')
        self.assertRaises(EPFloatOverBoundError, self.parser.parse, '1.1')
        self.assertRaises(EPFloatOverMaximumBoundError, self.parser.parse, '1.1')
    # endregion
    # endregion
