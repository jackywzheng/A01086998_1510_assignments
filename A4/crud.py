"""Assignment 04: CRUD."""

# Jacky Zheng
# A01086998
# 03/22/2019

from students import Student
import doctest


def add_student():
    """Create a student object and write it to students.txt if input is valid.

    PRECONDITION: User input must follow the Student Class requirements.
    POSTCONDITION: Instantiate a student object and write it to students.txt
    """
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    student_number = input("Enter the student number in the format of (A########): ")
    status_input = input("What is the student's status? Type '1' for True, '2' for False: ")
    status = True if status_input == "1" else False
    number_of_grades = input("Enter the student's grades each separated by a space : ")
    try:
        grades_list = []
        for each_grade in number_of_grades.split():
            grades_list.append(each_grade)
        new_student = Student(first_name, last_name, student_number, status, grades_list)
        file_write(new_student)
    except AttributeError:
        print("Error. You did not enter the correct information to add a new student. Returning to menu...")


def file_delete_student(deleted_student_number):
    """Return True if student number was found and deleted from students.txt, else return False.

    PARAM: deleted_student_number must be a string
    PRECONDITION: deleted_student_number must be a string in the form of A########
    RETURN: True if student number was deleted, False otherwise

    >>> file_delete_student('A0000000000')
    False
    """
    student_number_checker = []
    with open("students.txt", "r") as file_object:  # Have to read, and THEN write after. I tried "r+" but didn't work
        student_file = file_object.readlines()  # Create a list of each line as a string
        if deleted_student_number not in " ".join(student_file):  # Return False immediately if not in file string
            return False
    with open("students.txt", "w") as file_object:
        for line in student_file:
            if deleted_student_number not in line:  # If the line doesn't contain the student number, then rewrite it
                file_object.write(line)  # Writes the line only if the line doesn't contain the student number
                student_number_checker.append(line)  # Add it to new_student_file list so I can check if it was deleted
    if deleted_student_number in student_number_checker:  # If student number in checker, deletion failed
        return False
    else:  # If it's not in the new_student_file, then it was deleted
        return True


def file_read():
    """Return a list of student objects instantiated from students.txt.

    PRECONDITION: students.txt must be formatted correctly in the form of:
    Christopher Thompson A12345678 True 90 80 76 100 62 74
    RETURN: a list of student objects instantiated from students.txt
    """
    student_list = []
    with open("students.txt") as file_object:
        lines = file_object.readlines()  # Returns a list of lines
        for line in lines:  # Iterate through each line in the list
            final_grades = []
            for grades in line.split():  # Split the line into a list of tokens
                try:
                    final_grades.append(int(grades))
                except ValueError:
                    continue
            # Append each Student object to student_list by using the indexes in student_line to instantiate
            status = True if "True" in line else False
            student_object = Student(line.split()[0], line.split()[1], line.split()[2], status, final_grades)
            student_list.append(student_object)
    return student_list


def file_write(new_student):
    """Write a student object to students.txt.

    PARAM: new_student must be a valid student object.
    PRECONDITION: new_student must be a valid student object.
    POSTCONDITION: write the student object to students.txt
    """
    with open('students.txt', 'a') as file_object:
        file_object.write(str(new_student))


def add_grade():
    """Add a grade to a student in students.txt.

    PRECONDITION: input must follow Student Class requirements.
    RETURN: True if grade was added successfully, else False
    """
    student_number = input("Enter the student number: ")
    with open("students.txt") as file_object:  # Have to read, and THEN write after. I tried "r+" but didn't work
        student_file = file_object.readlines()  # Create a list of each line as a string
        if student_number not in "".join(student_file):
            return False
    with open("students.txt", "w") as file_object:
        for line in student_file:
            student_tokens = line.split()  # Create a list, add to list, make it into a string, write it
            if student_number in student_tokens:  # If the line doesn't contain the student number, then rewrite it
                student_grade = input("Enter the new grade you wish to add (Must be between 0 and 100): ")
                student_tokens.append(student_grade)
                file_object.write(" ".join(student_tokens) + "\n")
            else:
                file_object.write(line)
        return True


def calculate_class_average():
    """Return the class GPA of students.txt (Students without grades are not included in calculation).

    PRECONDITION: students.txt must be formatted correctly in the form of:
    Christopher Thompson A12345678 True 90 80 76 100 62 74
    RETURN: the class average rounded to two decimal places
    """
    student_list = file_read()  # Returns a list of student objects
    class_gpa = 0  # Acts as a counter to add student GPAs to
    students_with_gpa = 0  # Acts as a counter to count how many students have grades
    for student in student_list:
        if student.get_gpa() is not None:  # get_gpa() will return None if student object has no grades
            class_gpa += student.get_gpa()  # Add the GPA of each student with a GPA to class_gpa
            students_with_gpa += 1  # Add 1 to students_with_gpa
    return round(class_gpa / students_with_gpa, 2)  # Only counts students with a GPA


def print_class_list():
    """Prints the students in students.txt sorted by last name.

    PRECONDITION: students.txt must be formatted correctly in the form of:
    Christopher Thompson A12345678 True 90 80 76 100 62 74
    POSTCONDITION: prints the students in students.txt sorted by last name in the form of:
    Name: LastName , First Name | Student Number: A######## | Status: False | Grades: []
    """
    student_list = file_read()  # Returns a list of student objects
    sorting_list = []  # Create empty list for sorting purposes
    for student in student_list:
        # Append a list to sorting_list in the form of [last_name, StudentObject]
        sorting_list.append([student.get_last_name(), student])
    sorting_list.sort()  # Sort the sorting_list alphabetically
    for student in sorting_list:  # sorting_list now sorted, loop through list and print info of each student
        student[1].print_info()


def main():
    """Drives the program."""
    while True:
        choice = input("1. Add student\n2. Delete student\n3. Calculate class average\n"
                       "4. Print class list (sorted by last name)\n5. Add grade\n6. Quit")
        if choice == "1":
            try:
                add_student()
                print("Student successfully added!")
            except ValueError:
                print("Adding student failed due to invalid input. Returning to menu...")
        elif choice == "2":
            deleted_student_number = input("What is the student number that you wish to delete? ")
            if deleted_student_number[0] == "A" and deleted_student_number[1:9].isdigit() \
                    and len(deleted_student_number) == 9:
                delete_result = file_delete_student(deleted_student_number)
                if delete_result is True:
                    print("The student was deleted.")
                else:
                    print("Student number was not found. The student was not deleted.")
            else:
                print("Student number must be in the form of A########!")
        elif choice == "3":
            print("The class average is:", calculate_class_average())
        elif choice == "4":
            print_class_list()
        elif choice == "5":
            if add_grade():
                print("Grade successfully added!")
            else:
                print("Student number not found. Returning to menu...")
        elif choice == "6":
            break
        else:
            print("You did not enter a valid input. Please enter a valid input.")


if __name__ == '__main__':
    main()
    doctest.testmod()
