from epexceptions import NumericUnderMinimumError, IntUnderMinimumError, FloatUnderMinimumError, \
    NumericOverMaximumError, IntOverMaximumError, FloatOverMaximumError
from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPInt, EPFloat, EPComplex


class TestParsingString(TestParsing):
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

    def test_numeric_standard_easy_parse_type(self):
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

    def test_numeric_standard_with_numeric_under_minimum_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=EPInt(min=10)))

        # Assert
        with self.assertRaises(NumericUnderMinimumError):
            self.parser.parse('1')

        with self.assertRaises(IntUnderMinimumError):
            self.parser.parse('1')

        # Action
        self.parser.clear_args()
        self.parser.add_arg(Argument('a', argument_type=EPFloat(min=10)))

        # Assert
        with self.assertRaises(NumericUnderMinimumError):
            self.parser.parse('1.1')

        with self.assertRaises(FloatUnderMinimumError):
            self.parser.parse('1.1')

    def test_numeric_standard_with_numeric_over_maximum_error(self):
        # Action
        self.parser.add_arg(Argument('a', argument_type=EPInt(max=0)))

        # Assert
        with self.assertRaises(NumericOverMaximumError):
            self.parser.parse('1')

        with self.assertRaises(IntOverMaximumError):
            self.parser.parse('1')

        # Action
        self.parser.clear_args()
        self.parser.add_arg(Argument('a', argument_type=EPFloat(max=0)))

        # Assert
        with self.assertRaises(NumericOverMaximumError):
            self.parser.parse('1.1')

        with self.assertRaises(FloatOverMaximumError):
            self.parser.parse('1.1')


