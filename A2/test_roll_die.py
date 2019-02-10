"""Unit test for roll_die function"""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
import dungeonsanddragons


class TestRollDie(TestCase):
    # Tests if the sum of the rolls is greater than or equal to the minimum and less than or equal to the maximum roll
    def test_roll_die_maximum(self):
        self.assertTrue(3 * 1 <= dungeonsanddragons.roll_die(3, 6) <= 3 * 6)
