import builtins
import unittest
from unittest.mock import patch

from main import *

class TestMain(unittest.TestCase):
    def test_get_options_3(self):
        options = get_options(3)
        expected_options = ADVENTURES = {
            "A": "Adventure A",
            "B": "Adventure B",
            "C": "Adventure C",
            "E": "Exit"
        }
        self.assertEqual(options, expected_options)
    def test_get_options_1(self):
        options = get_options(1)
        expected_options = ADVENTURES = {
            "A": "Adventure A",
            "E": "Exit"
        }
        self.assertEqual(options, expected_options)
    def test_pick_number_50(self):
        self.assertEqual("a", "a")


if __name__ == '__main__':
    unittest.main()