"""Assignment 04: CRUD."""

# Jacky Zheng
# A01086998
# 03/22/2019


class Student:
    def __init__(self, first_name: str, last_name: str, student_number: str, status: str, final_grades: list):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.status = status
        self.final_grades = final_grades

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_number(self):
        return self.student_number

    def get_status(self):
        return self.status

    def get_final_grades(self):
        return self.final_grades

    def print_info(self):
        print("Name:", self.first_name, self.last_name, "Student Number: ", self.student_number,
              "Status: ", self.status, "Final grades: ", self.final_grades)


def add_student():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    student_number = input("Enter the student number: ")


def file_read():
    with open("students.txt") as file_object:
        file_object.read()


def file_write():
    with open("students.txt", 'w') as file_object:
        file_object.read()


def main():
    while True:
        choice = int(input("1. Add student\n2. Delete student\n"
                           "3. Calculate class average\n4. Print class list\n5. Quit"))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            print("You did not enter a valid input. Please enter a valid input.")


if __name__ == '__main__':
    main()
