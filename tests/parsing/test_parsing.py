import unittest

from epargument import EPArgument
from epparser import EPParser


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.parser = EPParser()
        self.parser.clear_args()

    def test_parsing_with_dest(self):
        # Assume
        assume = {'testDest': True}

        # Action
        self.parser.add_arg(EPArgument('a', dest='testDest', argument_type=bool))

        result = self.parser.parse('true')

        # Assert
        self.assertEqual(assume, result)
