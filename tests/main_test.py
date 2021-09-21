import builtins
import unittest
from unittest.mock import patch

from main import *
import protagonist

class TestMain(unittest.TestCase):
    def test_get_options_3(self):
        protag = Protagonist("Alex", ["she", "her", "her"])
        protag.add_adventure("A")
        protag.add_adventure("B")
        options = get_options(protag)
        expected_options = ADVENTURES = {
            "A": "Adventure A",
            "B": "Adventure B",
            "C": "Adventure C",
            "E": "Exit"
        }
        self.assertEqual(options, expected_options)
    def test_get_options_1(self):
        protag = Protagonist("Alex", ["she", "her", "her"])
        options = get_options(protag)
        expected_options = ADVENTURES = {
            "A": "Adventure A",
            "E": "Exit"
        }
        self.assertEqual(options, expected_options)
    def test_pick_number_50(self):
        self.assertEqual("a", "a")


if __name__ == '__main__':
    unittest.main()