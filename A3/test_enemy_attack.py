"""Unit test for enemy_attack function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud
from unittest.mock import patch


class TestPlayerAttack(TestCase):
    @patch('sud.roll_die', return_value=5)  # Berserker class takes double damage, so they take 10 damage
    def test_enemy_attack_berserker_player_dies(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.enemy_attack(player), 0)

    @patch('sud.roll_die', return_value=5)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_berserker_player_dies_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        expected_output = "==================================================================================" \
                          "=========================\nEnemy did 10 damage\nYou died\n"
        sud.enemy_attack(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=2)
    def test_enemy_attack_berserker_player_lives(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.enemy_attack(player), 6)

    @patch('sud.roll_die', return_value=2)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_berserker_player_lives_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        expected_output = "==================================================================================" \
                          "=========================\nEnemy did 4 damage\nYou now have 6 HP\n"
        sud.enemy_attack(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=6)  # All other classes deal regular damage
    def test_enemy_attack_saber_player_dies(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 6, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.enemy_attack(player), 0)

    @patch('sud.roll_die', return_value=6)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_saber_player_dies_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        expected_output = "==================================================================================" \
                          "=========================\nEnemy did 6 damage\nYou now have 4 HP\n"
        sud.enemy_attack(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=4)  # All other classes deal regular damage
    def test_enemy_attack_saber_player_lives(self, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.enemy_attack(player), 6)

    @patch('sud.roll_die', return_value=4)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_saber_player_lives_message(self, mock_stdout, mock_roll_die):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        expected_output = "==================================================================================" \
                          "=========================\nEnemy did 4 damage\nYou now have 6 HP\n"
        sud.enemy_attack(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
