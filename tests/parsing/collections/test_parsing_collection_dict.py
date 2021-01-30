from epexceptions import EPParsingFailedError, EPParsingDictFailedError, EPParsingCollectionFailedError, EPException, \
    EPValidationFailedError, EPValueOverBoundError, EPCollectionOverBoundError, EPDictOverBoundError, \
    EPDictOverMinimumBoundError, EPDictOverMaximumBoundError
from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPDict


class TestParsingCollectionDict(TestParsing):
    def test_dict_standard(self):
        # Assume
        assume = {'a': {'key1': '2', 'key3': '4', 'key5': '6'}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=dict))

        result = self.parser.parse('key1 2 key3 4 key5 6')

        # Assert
        self.assertEqual(assume, result)

    def test_dict_easy_parse_type(self):
        # Assume
        assume = {'a': {'key1': '2', 'key3': '4', 'key5': '6'}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPDict()))

        result = self.parser.parse('key1 2 key3 4 key5 6')

        # Assert
        self.assertEqual(assume, result)

    def test_dict_standard_sub_typed(self):
        # Assume
        assume = {'a': {'key1': 2, 'key3': 4, 'key5': 6}}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=dict[str, int]))

        result = self.parser.parse('key1 2 key3 4 key5 6')

        # Assert
        self.assertEqual(assume, result)

    # region Exceptions
    def test_dict_parsing_failed_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=dict[str, int]))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'key1 2 key3 4 key5')
        self.assertRaises(EPParsingFailedError, self.parser.parse, 'key1 2 key3 4 key5')
        self.assertRaises(EPParsingCollectionFailedError, self.parser.parse, 'key1 2 key3 4 key5')
        self.assertRaises(EPParsingDictFailedError, self.parser.parse, 'key1 2 key3 4 key5')

    def test_dict_over_minimum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPDict(min_size=3)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPValidationFailedError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPDictOverBoundError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPDictOverMinimumBoundError, self.parser.parse, 'key1 2 key3 4')

    def test_dict_over_maximum_bound_error(self):
        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPDict(max_size=1)))

        # Assert
        self.assertRaises(EPException, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPValidationFailedError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPValueOverBoundError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPCollectionOverBoundError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPDictOverBoundError, self.parser.parse, 'key1 2 key3 4')
        self.assertRaises(EPDictOverMaximumBoundError, self.parser.parse, 'key1 2 key3 4')
    # endregion
