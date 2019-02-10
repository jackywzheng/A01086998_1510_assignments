"""Unit test for create_character function."""

# Jacky Zheng
# A01086998
# 02/09/2019

import random
from unittest import TestCase
from unittest.mock import patch
import dungeonsanddragons


class TestCreateCharacter(TestCase):
    @patch('dungeonsanddragons.classes', return_value='druid')
    def test_create_character(self, mock_classes):
        random.seed(1)
        self.assertEqual(dungeonsanddragons.create_character(3),
                         {'Name': 'Exalat', 'Class': 'druid', 'HP': 1, 'Strength': 11, 'Dexterity': 10,
                          'Constitution': 12, 'Intelligence': 10, 'Wisdom': 9, 'Charisma': 10, 'XP': 0})

    @patch('dungeonsanddragons.classes', return_value='barbarian')
    def test_create_character_strength(self, mock_classes):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(3 <= character['Strength'] <= 18)

    @patch('dungeonsanddragons.classes', return_value='fighter')
    def test_create_character_dexterity(self, mock_classes):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(3 <= character['Dexterity'] <= 18)

    @patch('dungeonsanddragons.classes', return_value='druid')
    def test_create_character_constitution(self, mock_classes):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(3 <= character['Constitution'] <= 18)

    @patch('dungeonsanddragons.classes', return_value='cleric')
    def test_create_character_intelligence(self, mock_classes):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(3 <= character['Intelligence'] <= 18)

    @patch('dungeonsanddragons.classes', return_value='ranger')
    def test_create_character_wisdom(self, mock_classes):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(3 <= character['Wisdom'] <= 18)

    @patch('dungeonsanddragons.classes', return_value='rogue')
    def test_create_character_charisma(self, mock_classes):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(3 <= character['Charisma'] <= 18)

    @patch('dungeonsanddragons.classes', return_value='sorceror')
    @patch('dungeonsanddragons.class_hp', return_value='sorceror')  # How to do this one? I want to test chara dice
    def test_create_character_hp(self, mock_classes, mock_class_hp):
        character = dungeonsanddragons.create_character(1)
        self.assertTrue(1 <= character['HP'] <= 6)
