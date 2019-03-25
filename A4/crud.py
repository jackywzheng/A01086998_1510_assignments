"""Assignment 04: CRUD."""

# Jacky Zheng
# A01086998
# 03/22/2019


class Student:
    def __init__(self, first_name: str, last_name: str, student_number: str, status: str):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.status = status

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_number(self):
        return self.student_number

    def get_status(self):
        return self.status

    def print_info(self):
        print("Name:", self.first_name, self.last_name, "Student Number: ", self.student_number,
              "Status: ", self.status)


def add_student():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    student_number = input("Enter the student number: ")
    status = input("Enter the student's status (in good standing or not in good standing): ")
    try:
        new_student = Student(first_name, last_name, student_number, status)
        file_write(new_student)
    except TypeError:
        print("Error. You did not enter the required information to add a new student. Returning to menu.")


def file_delete_student(delete_student_number):
    with open("students.txt", "r+") as file_object:
        student_file = file_object.readlines()
        file_object.seek(0)
        for line in student_file:
            if line != delete_student_number:
                file_object.write(line)
                return True
            else:
                return False


def file_read():
    with open("students.txt") as file_object:
        file_object.readlines()


def file_write(new_student):
    with open("students.txt", 'a') as file_object:
        file_object.write(new_student.first_name + " " + new_student.last_name + " " +
                          new_student.student_number + " " + new_student.status + "\n")


def main():
    while True:
        choice = int(input("1. Add student\n2. Delete student\n"
                           "3. Calculate class average\n4. Print class list\n5. Quit"))
        if choice == 1:
            pass
        elif choice == 2:
            delete_student_number = input("What is the student number that you wish to delete? ")
            delete_result = file_delete_student(delete_student_number)
            if delete_result is True:
                print("The student has been deleted.")
            else:
                print("Student number was not found. The student was not deleted.")
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
