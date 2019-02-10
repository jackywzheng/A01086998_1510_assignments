"""Unit test for generate_vowel function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
import dungeonsanddragons


class TestGenerateVowel(TestCase):
    def test_generate_vowel(self):  # Vowel must be in this list
        self.assertIn(dungeonsanddragons.generate_vowel(), [['a'], ['e'], ['i'], ['o'], ['u'], ['y']])
