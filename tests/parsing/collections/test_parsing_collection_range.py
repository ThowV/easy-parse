from tests.parsing.test_parsing import TestParsing
from epargument import EPArgument
from eptypes import EPRange


class TestParsingCollectionRange(TestParsing):
    def test_range_standard(self):
        # Assume
        assume = {'a': range(0, 20, 2)}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=range))

        result = self.parser.parse('0 20 2')

        # Assert
        self.assertEqual(assume, result)

    def test_range_easy_parse_type(self):
        # Assume
        assume = {'a': range(1, 5)}

        # Action
        self.parser.add_arg(EPArgument('a', argument_type=EPRange()))

        result = self.parser.parse('1 5')

        # Assert
        self.assertEqual(assume, result)
