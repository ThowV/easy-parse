from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPSet


class TestParsingCollectionList(TestParsing):
    def test_set_standard(self):
        # Assume
        assume = {'a': {'a', '  trust', 'test', 'this is ', 'me'}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=set))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_set_easy_parse_type(self):
        # Assume
        assume = {'a': {'this is ', 'test', 'a'}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPSet(max_size=3)))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_set_standard_sub_typed(self):
        # Assume
        assume = {'a': {1, 2, 3}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=set[int]))

        result = self.parser.parse('1 2 3')

        # Assert
        self.assertEqual(assume, result)
