from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPDict


class TestParsingCollectionList(TestParsing):
    def test_dict_standard(self):
        # Assume
        assume = {'a': {'key1': '2', 'key3': '4', 'key5': '6'}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=dict))

        result = self.parser.parse('key1 2 key3 4 key5 6')

        # Assert
        self.assertEqual(assume, result)

    def test_dict_standard_with_easy_parse_type(self):
        # Assume
        assume = {'a': {'key1': '2', 'key3': '4'}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPDict(max_size=2)))

        result = self.parser.parse('key1 2 key3 4 key5 6')

        # Assert
        self.assertEqual(assume, result)

    def test_dict_with_sub_type(self):
        # Assume
        assume = {'a': {'key1': 2, 'key3': 4, 'key5': 6}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=dict[str, int]))

        result = self.parser.parse('key1 2 key3 4 key5 6')

        # Assert
        self.assertEqual(assume, result)
