from tests.parsing.test_parsing import TestParsing

from epargument import Argument
from eptypes import EPList


class TestParsingCollectionList(TestParsing):
    def test_list_standard(self):
        # Assume
        assume = {'a': ['this is ', 'a', 'test', '  trust', 'me']}

        # Action
        self.parser.add_arg(Argument('a', argument_type=list))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_list_standard_with_easy_parse_type(self):
        # Assume
        assume = {'a': ['this is ', 'a', 'test']}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPList(max_size=3)))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_list_with_sub_type(self):
        # Assume
        assume = {'a': [1, 2, 3]}

        # Action
        self.parser.add_arg(Argument('a', argument_type=list[int]))

        result = self.parser.parse('1 2 3')

        # Assert
        self.assertEqual(assume, result)
