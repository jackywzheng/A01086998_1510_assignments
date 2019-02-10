"""Unit test for generate_syllable function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
import dungeonsanddragons


class TestGenerateSyllable(TestCase):
    def test_generate_syllable(self):  # Length will always be 2 as it returns 1 vowel and 1 consonant
        self.assertTrue(len(dungeonsanddragons.generate_syllable()) == 2)

    def test_generate_syllable_vowel(self):  # First letter is a vowel. Can use a string as I used .join in the function
        syllable_vowel = dungeonsanddragons.generate_syllable()
        self.assertIn(syllable_vowel[0], 'aeiouy')

    def test_generate_syllable_consonant(self):  # First letter is consonant.
        syllable_consonant = dungeonsanddragons.generate_syllable()
        self.assertIn(syllable_consonant[1], 'bcdfghjklmnpqrstvwxyz')
