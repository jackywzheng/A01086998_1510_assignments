"""Unit test for combat_choice function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud
from unittest.mock import patch


class TestCombatChoice(TestCase):
    @patch('sud.roll_die', side_effect=[5, 4])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='no')
    def test_combat_choice_flee_and_take_damage(self, mock_roll_die, mock_stdout, input,):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = 'You have fled!\nYou took 4 damage while your back was turned!\n'
        sud.combat_choice(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=6)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='no')
    def test_combat_choice_flee_and_take_no_damage(self, mock_roll_die, mock_stdout, input,):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = 'You have fled!\n'
        sud.combat_choice(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.roll_die', return_value=6)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input',  side_effect=['lol', 'no'])
    def test_combat_choice_invalid_input(self, mock_roll_die, mock_stdout, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = "You did not type a valid input. Type 'yes' or 'no'.\nYou have fled!\n"
        sud.combat_choice(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.combat_round', return_value=None)  # Only want to test this function, so set return value as None
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='yes')
    def test_combat_choice_fight(self, input, mock_stdout, mock_combat_round):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        enemy = {'Name': 'Slime', 'HP': 5}
        expected_output = "The battle begins!\n"
        sud.combat_choice(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
