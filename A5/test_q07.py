from unittest import TestCase
from A5.q07 import password_validator


class TestPassword_validator(TestCase):
    def test_valid_password(self):
        self.assertTrue(password_validator("helloThere3"))

    def test_not_enough_length(self):
        self.assertFalse(password_validator("hello"))

    def test_empty_string(self):
        self.assertFalse(password_validator(""))

    def test_no_integer(self):
        self.assertFalse(password_validator("helloTherehowareyou"))

    def test_no_capital(self):
        self.assertFalse(password_validator("hellotherehowareyou3"))

    def test_no_lower_case(self):
        self.assertFalse(password_validator("HELLOTHERE3"))
