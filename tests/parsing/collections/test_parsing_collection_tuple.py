from typing import Tuple

from tests.parsing.test_parsing import TestParsing
from epargument import Argument
from eptypes import EPTuple


class TestParsingCollectionList(TestParsing):
    def test_list_standard(self):
        # Assume
        assume = {'a': ('string1', 2, 3.3, True, 'string4', 5, 6.6, True)}

        # Action
        self.parser.add_arg(Argument('a', argument_type=Tuple[str, int, float, bool]))

        result = self.parser.parse('string1 2 3.3 true string4 5 6.6 true')

        # Assert
        self.assertEqual(assume, result)

    def test_list_standard_with_easy_parse_type(self):
        # Assume
        assume = {'a': ('string1', 2, 3.3, True)}

        # Action
        self.parser.add_arg(Argument('a', argument_type=EPTuple([str, int, float, bool], max_size=1)))

        result = self.parser.parse('string1 2 3.3 true string4 5 6.6 true')

        # Assert
        self.assertEqual(assume, result)
