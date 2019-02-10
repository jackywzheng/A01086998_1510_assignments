
"""Unit test for roll_die function."""

# Jacky Zheng
# A01086998
# 02/04/2019

from unittest import TestCase
import dungeonsanddragons


class TestCreateName(TestCase):
    def test_create_name_length(self):
        self.assertTrue(len(dungeonsanddragons.generate_name(7)) == 14)  # Double length because vowel and consonant

    def test_create_name_first_letter_upper(self):
        upper_test = dungeonsanddragons.generate_name(10)
        self.assertTrue(upper_test[0].isupper())

    # Can also test if the ord() of letter is within a certain range in ASCII
    def test_create_name_ordinal(self):
        name = dungeonsanddragons.generate_name(10)
        for character in name:
            self.assertTrue(ord(character) in range(65, 91) or ord(character) in range(97, 123))
