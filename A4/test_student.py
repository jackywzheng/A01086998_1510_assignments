"""Student Class unit test."""

# Jacky Zheng
# A01086998
# 03/22/2019

from unittest import TestCase
from students import Student
import unittest.mock
import io


class TestStudent(TestCase):
    def setUp(self):
        self.test_student = Student("Jacky", "Zheng", "A01086998", True, ["100", "90", "80"])

    def test_get_first_name(self):
        self.assertEqual(self.test_student.get_first_name(), "Jacky")

    def test_get_last_name(self):
        self.assertEqual(self.test_student.get_last_name(), "Zheng")

    def test_get_student_number(self):
        self.assertEqual(self.test_student.get_student_number(), "A01086998")

    def test_get_status(self):
        self.assertEqual(self.test_student.get_status(), True)

    def test_get_grades(self):  # Also tests set_grades as I set these grades above
        self.assertEqual(self.test_student.get_grades(), ["100", "90", "80"])

    def test_get_gpa(self):
        self.assertEqual(self.test_student.get_gpa(), 90)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_info(self, mock_stdout):
        expected_output = \
            "Name: Zheng , Jacky | Student Number: A01086998 | Status: True | Grades: ['100', '90', '80']\n"
        self.test_student.print_info()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_reject_first_name_empty(self):
        with self.assertRaises(ValueError):
            Student("", "Zheng", "A01086998", True)

    def test_reject_last_name_empty(self):
        with self.assertRaises(ValueError):
            Student("Jacky", "", "A01086998", True)

    def test_reject_student_number(self):
        with self.assertRaises(ValueError):
            Student("Jacky", "Zheng", "A01089999999", True)

    def test_reject_status(self):
        with self.assertRaises(ValueError):
            Student("Jacky", "Zheng", "A01086998", "True")

    def test_set_first_name(self):
        self.test_student.set_first_name("Chris")
        self.assertEqual(self.test_student.get_first_name(), "Chris")

    def test_set_last_name(self):
        self.test_student.set_last_name("Thompson")
        self.assertEqual(self.test_student.get_last_name(), "Thompson")

    def test_set_grades(self):
        self.test_student.set_grades(['90', '70'])
        self.assertEqual(self.test_student.get_grades(), ['90', '70'])

    def test_set_status(self):
        self.test_student.set_status(False)
        self.assertEqual(self.test_student.get_status(), False)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test__str__(self, mock_stdout):
        expected_output = \
            "Jacky Zheng A01086998 True 100 90 80\n"
        self.assertEqual(str(self.test_student), expected_output)
