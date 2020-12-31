import unittest

from epparser import Parser


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.parser.clear_args()
