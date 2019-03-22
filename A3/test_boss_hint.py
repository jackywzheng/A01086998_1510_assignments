"""Unit test for boss_hint function."""

# Jacky Zheng
# A01086998
# 03/10/2019


from unittest import TestCase
import unittest.mock
import io
import sud


class TestBossHint(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_hint_displayed(self, mock_stdout):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 1, "Vertical": 3}
        expected_output = 'HINT: The boss lies in one of the 4 corners. Once you encounter him, ' \
                          'the battle will begin immediately.\n'
        sud.boss_hint(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_hint_not_displayed(self, mock_stdout):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        expected_output = ''
        sud.boss_hint(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
