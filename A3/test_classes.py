"""Unit test for classes function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import character
from unittest.mock import patch


class TestClasses(TestCase):
    @patch('builtins.input', return_value='Saber')
    def test_classes_saber(self, input):
        self.assertEqual(character.classes(), 'Saber')

    @patch('builtins.input', return_value='archer')
    def test_classes_archer(self, input):
        self.assertEqual(character.classes(), 'Archer')

    @patch('builtins.input', return_value='             LANCER')
    def test_classes_lancer(self, input):
        self.assertEqual(character.classes(), 'Lancer')

    @patch('builtins.input', return_value='   BeRsErKeR   ')
    def test_classes_berserker(self, input):
        self.assertEqual(character.classes(), 'Berserker')

    # The important message is on line 41: That is not a class, please select one of the 4 classes.
    @patch('builtins.input', side_effect=['Brawler', 'Saber'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_classes_invalid_input(self, mock_stdout, input):
        expected_output = "Here is a list of classes:\nSaber - A jack-of-all-trades warrior. Agile and powerful in " \
                          "close quarters; extremely adept at swordsmanship.\nArcher - Excellent scouts that excel " \
                          "in strategy and attacking from a distance. Masters of long ranged warfare.\nLancer - " \
                          "Gifted with extreme agility and proficient in hit-and-run tactics as well as ranged " \
                          "melee weapons such as spears and lances.\nBerserker - Mad Warrior. Crazed warriors that " \
                          "have lost almost all traces of their sanity in exchange for great power. " \
                          "(Deal and take 2x damage)\nThat is not a class, please select one of the 4 classes\n" \
                          "Here is a list of classes:\nSaber - A jack-of-all-trades warrior. Agile and powerful " \
                          "in close quarters; extremely adept at swordsmanship.\nArcher - Excellent scouts " \
                          "that excel in strategy and attacking from a distance. Masters of long ranged warfare.\n" \
                          "Lancer - Gifted with extreme agility and proficient in hit-and-run tactics as well " \
                          "as ranged melee weapons such as spears and lances.\nBerserker - Mad Warrior. Crazed " \
                          "warriors that have lost almost all traces of their sanity in exchange for great power. " \
                          "(Deal and take 2x damage)\n"
        character.classes()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
