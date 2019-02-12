"""Unit test for opponent_one_attack function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import dungeonsanddragons


class TestOpponentOneAttack(TestCase):
    # Tests when opponent_one passes Dexterity check, and depletes opponent_two's HP to 0 or below
    @patch('dungeonsanddragons.roll_die', return_value=18)  # Dexterity check always passes
    @patch('dungeonsanddragons.class_hp', return_value=4)  # Damage always more than opponent_two's HP
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_opponent_one_attack_opponent_two_died(self, mock_stdout, mock_roll_die, mock_class_hp):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 3, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                        'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You rolled a 18 and passed the Dexterity check. You did 4 damage\nEnemy has died\n'
        dungeonsanddragons.opponent_one_attack(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Tests when opponent_one passes Dexterity check, and opponent_two's HP is greater than 0
    @patch('dungeonsanddragons.roll_die', return_value=18)  # Dexterity check always passes
    @patch('dungeonsanddragons.class_hp', return_value=2)  # Damage always less than opponent_two's HP
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_opponent_one_attack_opponent_two_alive(self, mock_stdout, mock_roll_die, mock_class_hp):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 3, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                        'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You rolled a 18 and passed the Dexterity check. You did 2 damage\nEnemy now has 1 HP\n'
        dungeonsanddragons.opponent_one_attack(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Tests when opponent_one fails Dexterity check
    @patch('dungeonsanddragons.roll_die', return_value=3)  # Dexterity check failed, lower than opponent_two's Dexterity
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_opponent_one_attack_failed(self, mock_stdout, mock_roll_die):
        opponent_one = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18
                        , 'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        opponent_two = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 3, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                        'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You rolled a 3 and failed the Dexterity check\n'
        dungeonsanddragons.opponent_one_attack(opponent_one, opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
