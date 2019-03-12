"""Unit test for classes function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import sud
import monster
from unittest.mock import patch


class TestMonsterPicker(TestCase):
    @patch('sud.roll_die', return_value=1)
    def test_monster_picker_slime(self, mock_roll_die):
        self.assertEqual(monster.monster_picker(), {'Name': 'Slime', 'HP': 5})

    @patch('sud.roll_die', return_value=2)
    def test_monster_picker_table_flipper(self, mock_roll_die):
        self.assertEqual(monster.monster_picker(), {'Name': 'Table Flipper', 'HP': 5})

    @patch('sud.roll_die', return_value=3)
    def test_monster_picker_werebear(self, mock_roll_die):
        self.assertEqual(monster.monster_picker(), {'Name': 'Cat', 'HP': 5})

    @patch('sud.roll_die', return_value=4)
    def test_monster_picker_cat(self, mock_roll_die):
        self.assertEqual(monster.monster_picker(), {'Name': 'Werebear', 'HP': 5})
