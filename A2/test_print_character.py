"""Unit test for print_character function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
import unittest.mock
import io
import dungeonsanddragons


class TestPrintCharacter(TestCase):
    # Have to type it in this weird format otherwise it won't match
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        character = {'Name': 'Ajokixav', 'Class': 'bard', 'HP': 1, 'Strength': 12, 'Dexterity': 13, 'Constitution': 8,
                     'Intelligence': 10, 'Wisdom': 8, 'Charisma': 13, 'XP': 0}
        expected_output = """Name: Ajokixav
Class: bard
HP: 1
Strength: 12
Dexterity: 13
Constitution: 8
Intelligence: 10
Wisdom: 8
Charisma: 13
XP: 0
"""
        dungeonsanddragons.print_character(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
