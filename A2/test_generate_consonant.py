"""Unit test for generate_vowel function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
import dungeonsanddragons


class TestGenerateConsonant(TestCase):
    def test_generate_consonant(self):  # Consonant must be in this list
        self.assertIn(dungeonsanddragons.generate_consonant(), [['b'], ['c'], ['d'], ['f'], ['g'], ['h'], ['j'], ['k'],
                                                                ['l'], ['m'], ['n'], ['p'], ['q'], ['r'], ['s'], ['t'],
                                                                ['v'], ['w'], ['x'], ['y'], ['z']])

    def test_generate_consonant_string(self):
        consonant = dungeonsanddragons.generate_consonant()
        self.assertTrue((type(consonant[0]) is str))
