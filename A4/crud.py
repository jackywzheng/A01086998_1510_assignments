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
        self.grades = []

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_number(self):
        return self.student_number

    def get_status(self):
        return self.status

    def get_grades(self):
        return self.grades

    def get_gpa(self):
        gpa = 0
        for grades in self.grades:
            gpa += grades
        try:
            return round(gpa / len(self.grades), 2)
        except ZeroDivisionError:
            return None

    def print_info(self):
        print("Name:", self.first_name, self.last_name, "Student Number:", self.student_number,
              "Status:", self.status, "Grades:", self.grades)


def add_student():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    student_number = input("Enter the student number: ")
    status = input("Enter the student's status (in-good-standing or not-in-good-standing): ")
    try:
        new_student = Student(first_name, last_name, student_number, status)
        file_write(new_student)
    except TypeError:
        print("Error. You did not enter the required information to add a new student. Returning to menu.")


def file_delete_student(delete_student_number):
    with open("students.txt", "r+") as file_object:
        student_file = file_object.readlines()
        for line in student_file:
            if line != delete_student_number:
                file_object.write(line)  # Writes whole list


def file_read():
    student_list = []
    with open("students.txt") as file_object:
        lines = file_object.readlines()  # Returns a list of lines
        for line in lines:  # Iterate through each line in the list
            student_line = line.split()  # Split the line into a list of tokens
            final_grades = []
            for grades in student_line:
                try:
                    final_grades.append(int(grades))
                except ValueError:
                    pass
            # Append each Student object to student_list by using the indexes in student_line to instantiate
            student_object = Student(student_line[0], student_line[1], student_line[2], student_line[3])
            setattr(student_object, "grades", final_grades)
            student_list.append(student_object)
    return student_list


def print_class_list():
    with open("students.txt") as file_object:
        lines = file_object.readlines()
        for line in lines:
            student_line = line.split()
            print(student_line)


def file_write(new_student):
    with open("students.txt", 'a') as file_object:
        file_object.write(new_student.first_name + " " + new_student.last_name + " " +
                          new_student.student_number + " " + new_student.status + "\n")


def main():
    while True:
        choice = int(input("1. Add student\n2. Delete student\n"
                           "3. Calculate class average\n4. Print class list\n5. Quit"))
        if choice == 1:
            add_student()
        elif choice == 2:
            delete_student_number = input("What is the student number that you wish to delete? ")
            delete_result = file_delete_student(delete_student_number)
            if delete_result is True:
                print("The student was deleted.")
            else:
                print("Student number was not found. The student was not deleted.")
        elif choice == 3:
            student_list = file_read()
            class_gpa = 0
            for student in student_list:
                print(student.get_first_name(), student.get_last_name() + "'s GPA is:", student.get_gpa())
                if student.get_gpa() is not None:
                    class_gpa += student.get_gpa()
            print("The class average is:", round(class_gpa/len(student_list), 2))
        elif choice == 4:
            print("Class list in a meaningful way")
        elif choice == 5:
            break
        else:
            print("You did not enter a valid input. Please enter a valid input.")


if __name__ == '__main__':
    main()
