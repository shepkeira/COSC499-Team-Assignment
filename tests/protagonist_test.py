import builtins
import unittest
from unittest.mock import patch

from protagonist import *

class TestProtagonist(unittest.TestCase):
     def test_init_works(self):
        mary = Protagonist("Mary", ["she", "her", "her"])
        mary_pronouns = "Does this sound correct? \'" + mary.subject_pronoun +" has " + mary.possessive_pronoun + " sword with " + mary.object_pronoun + "\'"
        expected_mary_pro = "Does this sound correct? \'she has her sword with her\'"
        max = Protagonist("Max", ["they", "them", "their"])
        max_pronouns = "Does this sound correct? \'" + max.subject_pronoun +" has " + max.possessive_pronoun + " sword with " + max.object_pronoun + "\'"
        expected_max_pro = "Does this sound correct? \'they has their sword with them\'"
        jon = Protagonist("Jon", ["he", "him", "his"])
        jon_pronouns = "Does this sound correct? \'" + jon.subject_pronoun +" has " + jon.possessive_pronoun + " sword with " + jon.object_pronoun + "\'"
        expected_jon_pro = "Does this sound correct? \'he has his sword with him\'"
        
        
        self.assertEqual(mary.name, "Mary")
        self.assertEqual(max.name, "Max")
        self.assertEqual(jon.name, "Jon")
        self.assertEqual(expected_mary_pro, mary_pronouns)
        self.assertEqual(expected_jon_pro, jon_pronouns)
        self.assertEqual(expected_max_pro, max_pronouns)


if __name__ == '__main__':
    unittest.main()