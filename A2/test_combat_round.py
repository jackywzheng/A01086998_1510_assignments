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
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 1, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        with self.assertRaises(RecursionError):
            dungeonsanddragons.combat_round(character_1, character_2)

    # This tests for when character_1 successfully attacks character_2, but character_2 has remaining HP
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 4])  # Char 1 always goes first as he rolls 5, Char 2 rolls 4
    @patch('dungeonsanddragons.class_hp', return_value=4)  # 4 is the damage roll
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_2_remaining_HP(self, mock_stdout, mock_roll_die, mock_class_hp):
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 5, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'Enemy now has 1 HP\n'
        dungeonsanddragons.combat_round(character_1, character_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when character_1 successfully attacks character_2, resulting in character_2 HP <= 0 (death)
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 4])
    @patch('dungeonsanddragons.class_hp', return_value=4)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_2_dead(self, mock_stdout, mock_roll_die, mock_class_hp):
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 3, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'Enemy has died\n'
        dungeonsanddragons.combat_round(character_1, character_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when character_1 fails their attack, because character_2 Dexterity is higher
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 4])
    @patch('dungeonsanddragons.class_hp', return_value=4)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_1_attack_fail(self, mock_stdout, mock_roll_die, mock_class_hp):
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 1, 'Strength': 3, 'Dexterity': 5, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'Your attack failed\n'
        dungeonsanddragons.combat_round(character_1, character_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when character_2 successfully attacks character_1, but character_1 has remaining HP
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 19])
    @patch('dungeonsanddragons.class_hp', return_value=8)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_1_remaining_HP(self, mock_stdout, mock_roll_die, mock_class_hp):
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 1, 'Strength': 3, 'Dexterity': 5, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You now have 1 HP\n'
        dungeonsanddragons.combat_round(character_1, character_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when character_2 successfully attacks character_1, resulting in character_1 HP <= 0 (death)
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 19])
    @patch('dungeonsanddragons.class_hp', return_value=8)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_1_dead(self, mock_stdout, mock_roll_die, mock_class_hp):
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 8, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 3, 'Strength': 3, 'Dexterity': 3, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'You died\n'
        dungeonsanddragons.combat_round(character_1, character_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # This tests for when character_2 fails their attack, because character_1 Dexterity is higher
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 18])
    @patch('dungeonsanddragons.class_hp', return_value=8)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_2_attack_fail(self, mock_stdout, mock_roll_die, mock_class_hp):
        character_1 = {'Name': 'Jaki', 'Class': 'fighter', 'HP': 9, 'Strength': 18, 'Dexterity': 18, 'Constitution': 18,
                       'Intelligence': 18, 'Wisdom': 18, 'Charisma': 18, 'XP': 0}
        character_2 = {'Name': 'Kurisu', 'Class': 'bard', 'HP': 1, 'Strength': 3, 'Dexterity': 5, 'Constitution': 3,
                       'Intelligence': 3, 'Wisdom': 3, 'Charisma': 3, 'XP': 0}
        expected_output = 'Enemy attack failed\n'
        dungeonsanddragons.combat_round(character_1, character_2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
