"""Unit test for combat_round function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dungeonsanddragons


class TestCombatRound(TestCase):
    # This test will generate a recursion error as the function will continue calling itself as it will always roll 9
    @patch('dungeonsanddragons.roll_die', return_value=9)
    def test_combat_round_ties(self, mock_roll_die):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 1, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                        'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        with self.assertRaises(RecursionError):
            dungeonsanddragons.combat_round(opponent_one, opponent_two)

    # This tests when opponent_one attacks first
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 4])  # Char 1 always goes first as he rolls 5, Char 2 rolls 4
    @patch('dungeonsanddragons.opponent_one_attack', return_value=1)  # Always set as 1 because not always returning
    @patch('dungeonsanddragons.opponent_two_attack', return_value=1)  # Always set as 1 because not always returning
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_one_attack_first(self, mock_stdout, mock_roll_die,
                                                   mock_opponent_one_attack, mock_opponent_two_attack):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 5, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3
                        , 'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You rolled 5\nEnemy rolled 4\nYou strike first\n'
        dungeonsanddragons.combat_round(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when opponent_two attacks first
    @patch('dungeonsanddragons.roll_die', side_effect=[4, 5])
    @patch('dungeonsanddragons.opponent_one_attack', return_value=1)
    @patch('dungeonsanddragons.opponent_two_attack', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_two_attack_first(self, mock_stdout, mock_roll_die,
                                           mock_opponent_one_attack, mock_opponent_two_attack):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 3, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3
                        , 'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You rolled 4\nEnemy rolled 5\nEnemy strikes first\n'
        dungeonsanddragons.combat_round(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when opponent_two dies, Combat ended should be printed
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 4])
    @patch('dungeonsanddragons.opponent_one_attack', return_value=1)
    @patch('dungeonsanddragons.opponent_two_attack', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_two_dies(self, mock_stdout, mock_roll_die,
                                            mock_opponent_one_attack, mock_opponent_two_attack):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': -2, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                        'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}  # Updated HP here
        expected_output = 'You rolled 5\nEnemy rolled 4\nYou strike first\nCombat ended\n'
        dungeonsanddragons.combat_round(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when opponent_one dies, Combat ended should be printed
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 4])
    @patch('dungeonsanddragons.opponent_one_attack', return_value=1)
    @patch('dungeonsanddragons.opponent_two_attack', return_value=1)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_opponent_one_dies(self, mock_stdout, mock_roll_die,
                                            mock_opponent_one_attack, mock_opponent_two_attack):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': -1, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}  # Updated HP here
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': -2, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                        'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You rolled 5\nEnemy rolled 4\nYou strike first\nCombat ended\n'
        dungeonsanddragons.combat_round(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
