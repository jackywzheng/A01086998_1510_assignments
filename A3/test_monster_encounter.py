"""Unit test for monster_encounter function."""

# Jacky Zheng
# A01086998
# 03/10/2019


from unittest import TestCase
from unittest.mock import patch
import sud


class TestMonsterEncounter(TestCase):
    @patch('sud.roll_die', return_value=5)  # If a 5 is rolled, then there is an encounter
    def test_monster_encounter_true(self, mock_roll_die):
        self.assertEqual(sud.monster_encounter(), True)

    @patch('sud.roll_die', return_value=6)  # If anything but a 5 is rolled, then there is no encounter
    def test_monster_encounter_false(self, mock_roll_die):
        self.assertEqual(sud.monster_encounter(), False)
