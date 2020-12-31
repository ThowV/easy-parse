from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPFrozenSet


class TestParsingCollectionList(TestParsing):
    def test_frozenset_standard(self):
        # Assume
        assume = {'a': {'a', '  trust', 'test', 'this is ', 'me'}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=frozenset))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_frozenset_standard_with_easy_parse_type(self):
        # Assume
        assume = {'a': {'this is ', 'a', 'test'}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPFrozenSet(max_size=3)))

        result = self.parser.parse('"this is " a test "  trust" me')

        # Assert
        self.assertEqual(assume, result)

    def test_frozenset_with_sub_type(self):
        # Assume
        assume = {'a': {1, 2, 3}}

        # Action
        self.parser.add_arg(Argument('a', argument_type=frozenset[int]))

        result = self.parser.parse('1 2 3')

        # Assert
        self.assertEqual(assume, result)
