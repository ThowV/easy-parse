import unittest

from epargument import Argument
from epparser import Parser


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.parser.clear_args()

    def test_parsing_with_dest(self):
        # Assume
        assume = {'testDest': True}

        # Action
        self.parser.add_arg(Argument('a', dest='testDest', argument_type=bool))

        result = self.parser.parse('true')

        # Assert
        self.assertEqual(assume, result)
