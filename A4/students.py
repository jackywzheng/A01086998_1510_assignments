"""Unit test for Student Class."""

# Jacky Zheng
# A01086998
# 03/22/2019


class Student:
    """Represents a simple BCIT student."""
    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list = None):
        """Create a new student. A student must have a non-empty first and last name and will be stored as title case.
        A student must also have a student number in the format of 'A########'. A student must also have a status
        stored as a boolean to represent whether or not the student is in good-standing. The student can also have
        an optional list of grades between 0 and 100. If no grades are provided, the student will be assigned an
        empty list of grades. If any of the above requirements are not met, a ValueError will be raised and the
        student object will not instantiate."""
        if len(first_name) != 0 and len(last_name) != 0:
            self.__first_name = first_name.strip().title()
            self.__last_name = last_name.strip().title()
        else:
            raise ValueError("Names cannot be empty!")
        if student_number[0] == "A" and student_number[1:9].isdigit() and len(student_number) == 9:
            self.__student_number = student_number.strip().title()
        else:
            raise ValueError("Student number must be in the form of A########!")
        if status is True or status is False:
            self.__status = status
        else:
            raise ValueError("Status must be True or False")
        if grades is None:
            self.__grades = []
        elif type(grades) is list:
            self.__grades = grades
        else:
            raise ValueError("Grades must be a list!")

    # Accessors
    def get_first_name(self):
        """Return the first name."""
        return self.__first_name

    def get_last_name(self):
        """Return the last name."""
        return self.__last_name

    def get_student_number(self):
        """Return the student number."""
        return self.__student_number

    def get_status(self):
        """Return the status."""
        return self.__status

    def get_grades(self):
        """Return the grades."""
        return self.__grades

    def get_gpa(self):
        """Return the GPA rounded to two decimal points."""
        if len(self.__grades) == 0:  # If empty list, then return None
            return None
        gpa = 0
        for grades in self.__grades:
            gpa += int(grades)
        return round(gpa / len(self.__grades), 2)  # Else return the GPA

    # Mutators
    def set_grades(self, grades: list):
        """Set the grades if it is valid."""
        if type(grades) is list:
            self.__grades = grades
        else:
            raise ValueError("Grades must be a list!")

    def set_first_name(self, first_name: str):
        """Set the first name if it is valid."""
        if len(first_name) != 0:
            self.__first_name = first_name.strip().title()
        else:
            raise ValueError("Names cannot be empty!")

    def set_last_name(self, last_name: str):
        """Set the last name if it is valid."""
        if len(last_name) != 0:
            self.__last_name = last_name.strip().title()
        else:
            raise ValueError("Names cannot be empty!")

    def set_status(self, status: bool):
        """Set the status if it is valid."""
        if status is True or status is False:
            self.__status = status
        else:
            raise ValueError("Status must be True or False")

    def print_info(self):
        """Print the student information in the following format:
        Name: LastName , First Name | Student Number: A######## | Status: True | Grades: 100 90 80."""
        print("Name:", self.__last_name, ",", self.__first_name, "| Student Number:", self.__student_number,
              "| Status:", self.__status, "| Grades:", self.__grades)

    def __str__(self):
        """Return a string representation of this student that looks like:
        FirstName LastName A######## True 90 80 76 100 62 42
        Useful for the print function."""
        student_info = self.__first_name + " " + self.__last_name + " " + \
                       self.__student_number + " " + str(self.__status) + " " + " ".join(self.__grades) + "\n"
        return student_info
