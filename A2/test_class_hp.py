"""Unit test for class_HP function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
import dungeonsanddragons


class TestClassHP(TestCase):
    def test_class_hp_barbarian(self):
        self.assertTrue(1 <= dungeonsanddragons.class_hp('barbarian') <= 12)  # Barbarian is a d12

    def test_class_hp_paladin(self):
        self.assertTrue(1 <= dungeonsanddragons.class_hp('paladin') <= 10)  # Paladin is a d10

    def test_class_hp_druid(self):
        self.assertTrue(1 <= dungeonsanddragons.class_hp('druid') <= 8)  # Druid is a d8

    def test_class_hp_sorcerer(self):
        self.assertTrue(1 <= dungeonsanddragons.class_hp('sorcerer') <= 6)  # Sorcerer is a d6
