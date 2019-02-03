from unittest import TestCase
import time_calculator


class TestTimeCalculator(TestCase):
    def test_time_calculator_1_of_each(self):
        self.assertEqual([1, 1, 1, 59], time_calculator.time_calculator(90119))

    def test_time_calculator_1_minute_1_seconds(self):
        self.assertEqual([0, 0, 1, 1], time_calculator.time_calculator(61))

    def test_time_calculator_1_hour_1_second(self):
        self.assertEqual([0, 1, 0, 1], time_calculator.time_calculator(3601))

    def test_time_calculator_1_day_1_second(self):
        self.assertEqual([1, 0, 0, 1], time_calculator.time_calculator(86401))
