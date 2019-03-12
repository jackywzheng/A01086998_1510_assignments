"""Unit test for combat_round function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud
from unittest.mock import patch


class TestCombatRound(TestCase):
    @patch('sud.roll_die', return_value=1)
    @patch('sud.player_attack', return_value=0)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_player_attack_first_and_slays_monster(self, mock_stdout, mock_roll_die, mock_player_attack):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 0}
        expected_output = 'You attack first\nYou have slain the monster\n'
        sud.combat_round(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=2)
    @patch('sud.enemy_attack', return_value=0)
    def test_combat_round_enemy_attack_first_and_player_dies(self, mock_roll_die, mock_enemy_attack):
        player = {"Name": 'Jacky', "HP": 0, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        self.assertEqual(sud.combat_round(player, enemy), None)
