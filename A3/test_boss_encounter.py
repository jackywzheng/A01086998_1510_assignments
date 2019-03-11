"""Unit test for boss_encounter function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud
from unittest.mock import patch


class TestBossEncounter(TestCase):
    @patch('sud.combat_round', return_value=True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='An A in Python')
    def test_boss_encounter_win_message(self, mock_combat_round, mock_stdout, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 4, "Vertical": 4}
        expected_output = "You have found the Holy Grail! However, a strong monster stands between you and the Holy " \
                          "Grail. Defeat the monster to claim the Holy Grail and fulfill your wish!\nYou have " \
                          "encountered a Great Old One, Cthulu! ^(;,;)^ It has 15 HP.\nYou take a drink from " \
                          "the Holy Grail in order for it to grant your wish, only to discover that\nit's just " \
                          "watermelon juice. You feel cheated, but at least your thirst was quenched." \
                          "Thanks for playing!\n"
        sud.boss_encounter(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.combat_round', return_value=False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='An A in Python')
    def test_boss_encounter_lose_message(self, mock_combat_round, mock_stdout, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 4, "Vertical": 4}
        expected_output = "You have found the Holy Grail! However, a strong monster stands between you and the Holy " \
                          "Grail. Defeat the monster to claim the Holy Grail and fulfill your wish!\nYou have " \
                          "encountered a Great Old One, Cthulu! ^(;,;)^ It has 15 HP.\n"
        sud.boss_encounter(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sud.combat_round', return_value=True)
    @patch('builtins.input', return_value='An A in Python')
    def test_boss_encounter_win(self, mock_combat_round, input):
        self.assertEqual(sud.boss_encounter({"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 4,
                                             "Vertical": 4}), True)

    @patch('sud.combat_round', return_value=False)
    @patch('builtins.input', return_value='An A in Python')
    def test_boss_encounter_lose(self, mock_combat_round, input):
        self.assertEqual(sud.boss_encounter({"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 4,
                                             "Vertical": 4}), None)
