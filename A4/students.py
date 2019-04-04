"""Unit test for Student Class."""

# Jacky Zheng
# A01086998
# 03/22/2019


class Student:
    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list = None):
        if len(first_name) != 0 and len(last_name) != 0:
            self.__first_name = first_name
            self.__last_name = last_name
        else:
            raise ValueError("Names must only contain letters!")
        if student_number[0] == "A" and student_number[1:9].isdigit() and len(student_number) == 9:
            self.__student_number = student_number
        else:
            raise ValueError("Student number must be in the form of A########!")
        if status is True or status is False:
            self.__status = status
        else:
            raise ValueError("Status must be True or False")
        if grades is None:
            self.__grades = []
        else:
            self.__grades = grades

    # Accessors
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_number(self):
        return self.__student_number

    def get_status(self):
        return self.__status

    def get_grades(self):
        return self.__grades

    def get_gpa(self):
        if len(self.__grades) == 0:  # If empty list, then return None
            return None
        gpa = 0
        for grades in self.__grades:
            gpa += int(grades)
        return round(gpa / len(self.__grades), 2)  # Else return the GPA

    # Mutators
    def set_grades(self, grades):
        self.__grades = grades

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def print_info(self):
        print("Name:", self.__last_name, ",", self.__first_name, "| Student Number:", self.__student_number,
              "| Status:", self.__status, "| Grades:", self.__grades)

    def __str__(self):
        student_info = self.__first_name + " " + self.__last_name + " " + \
                       self.__student_number + " " + str(self.__status) + " " + " ".join(self.__grades) + "\n"
        return student_info
