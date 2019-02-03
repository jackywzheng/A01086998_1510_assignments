"""Unit test for lotto."""

# Jacky Zheng
# A01086998
# 01/30/19

from unittest import TestCase
import lotto


class TestNumberGenerator(TestCase):
    def test_number_generator_sorted_and_unique(self):
        lottery = lotto.number_generator()
        self.assertTrue(lottery[0] < lottery[1] < lottery[2] < lottery[3] < lottery[4] < lottery[5])
        # I assign function to a variable and test in sequential order as they are already sorted.
        # This confirms that all numbers are unique and correctly sorted

    def test_number_generator_6_numbers(self):
        self.assertTrue(len(lotto.number_generator()) == 6, lotto.number_generator())
        # Length of the list is 6, confirming there are 6 numbers

    def test_number_generator_integer(self):
        self.assertTrue(int, type(sum(lotto.number_generator())))
        # Adds the values inside the list and compares if it's an integer

    def test_number_generator_between_1_to_49(self):
        lottery = lotto.number_generator()
        self.assertTrue(lottery[0] > 0 and lottery[5] < 50)
        # Take the smallest and largest number and confirms it's greater than 0 and less than 50





