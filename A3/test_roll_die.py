"""Unit test for roll_die function."""

# Jacky Zheng
# A01086998
# 03/10/2019


from unittest import TestCase
import sud


class TestRollDie(TestCase):
    # Tests if the sum of the rolls is greater than or equal to the minimum AND less than or equal to the maximum roll
    def test_roll_die_between_min_and_max(self):
        self.assertTrue(3 * 1 <= sud.roll_die(3, 6) <= 3 * 6)

    def test_roll_die_integer(self):
        self.assertTrue(type(sud.roll_die(3, 6)) is int)
