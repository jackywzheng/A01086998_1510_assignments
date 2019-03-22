"""Unit test for hp_recovery function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import character


class TestHPRecovery(TestCase):
    # Recover 1 HP and return new HP
    def test_hp_recovery_less_than_10(self):
        my_character = {"Name": 'Jacky', "HP": 9, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(character.hp_recovery(my_character), 10)

    def test_hp_recovery_at_10(self):
        my_character = {"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(character.hp_recovery(my_character), None)

    def test_hp_recovery_more_than_10(self):
        my_character = {"Name": 'Jacky', "HP": 11, "Class": "Saber", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(character.hp_recovery(my_character), None)
