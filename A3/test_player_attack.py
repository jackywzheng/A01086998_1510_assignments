"""Unit test for player_attack function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud
from unittest.mock import patch


class TestPlayerAttack(TestCase):
    @patch('sud.roll_die', return_value=5)  # Berserker class deals double damage, so it does 10 damage
    def test_player_attack_berserker_enemy_dies(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        self.assertEqual(sud.player_attack(player, enemy), -5)

    @patch('sud.roll_die', return_value=5)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_berserker_enemy_dies_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = "==================================================================================" \
                          "=========================\nYou did 10 damage\nEnemy has died\n"
        sud.player_attack(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=2)
    def test_player_attack_berserker_enemy_lives(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        self.assertEqual(sud.player_attack(player, enemy), 1)

    @patch('sud.roll_die', return_value=2)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_berserker_enemy_lives_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = "==================================================================================" \
                          "=========================\nYou did 4 damage\nEnemy now has 1 HP\n"
        sud.player_attack(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=5)  # All other classes deal regular damage
    def test_player_attack_saber_enemy_dies(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        self.assertEqual(sud.player_attack(player, enemy), 0)

    @patch('sud.roll_die', return_value=6)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_saber_enemy_dies_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = "==================================================================================" \
                          "=========================\nYou did 6 damage\nEnemy has died\n"
        sud.player_attack(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=4)  # All other classes deal regular damage
    def test_player_attack_saber_enemy_lives(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        self.assertEqual(sud.player_attack(player, enemy), 1)

    @patch('sud.roll_die', return_value=4)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_saber_enemy_lives_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = "==================================================================================" \
                          "=========================\nYou did 4 damage\nEnemy now has 1 HP\n"
        sud.player_attack(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
