"""Assignment 04: CRUD."""

# Jacky Zheng
# A01086998
# 03/22/2019


class Student:
    def __init__(self, first_name: str, last_name: str, student_number: str, status: str):
        if first_name.isalpha() and last_name.isalpha():
            self.__first_name = first_name
            self.__last_name = last_name
        else:
            raise ValueError("Names must only contain letters!")
        if student_number[0] == "A" and student_number[1:9].isdigit():
            self.__student_number = student_number
        else:
            raise ValueError("Student number must be in the form of A########!")
        if status == "True" or status == "False":
            self.__status = status
        else:
            raise ValueError("Status must be True or False")
        self.__grades = []

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
        if self.__grades is []:
            return None
        gpa = 0
        for grades in self.__grades:
            gpa += grades
            return round(gpa / len(self.__grades), 2)

    def set_grades(self, grades):
        self.__grades = grades

    def print_info(self):
        print("Name:", self.__first_name, self.__last_name, "Student Number:", self.__student_number,
              "Status:", self.__status, "Grades:", self.__grades,
              "\n========================================================================================")

    def __str__(self):
        student_info = self.__first_name + " " + self.__last_name + " " + \
                       self.__student_number + " " + self.__status + " " + " ".join(self.__grades) + "\n"
        return student_info


def add_student():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    student_number = input("Enter the student number in the format of (A########): ")
    status = input("Enter the student's status (True or False): ")
    number_of_grades = int(input("Enter the number of student's grades that you wish to add: "))
    try:
        new_student = Student(first_name.strip(), last_name.strip(), student_number.strip(), status.strip())
        if number_of_grades > 0:
            grades_list = []
            for i in range(number_of_grades):
                grades = input("Enter a grade: ")
                grades_list.append(grades)
            new_student.set_grades(grades_list)
            file_write(new_student)
    except AttributeError:
        print("Error. You did not enter the required information to add a new student. Returning to menu.")


def file_delete_student(delete_student_number):
    new_student_file = []
    with open("students.txt", "r") as file_object:  # Have to read, and THEN write after. I tried "r+" but didn't work
        student_file = file_object.readlines()  # Create a list of each line as a string
    with open("students.txt", "w") as file_object:
        for line in student_file:
            if delete_student_number not in line:  # If the line doesn't contain the student number, then rewrite it
                file_object.write(line)  # Writes the line only if the line doesn't contain the student number
                new_student_file.append(line)  # Add it to new_student_file list so I can check if it was deleted
    if delete_student_number not in student_file:  # If it wasn't in student_file, then return False as it doesn't exist
        return False
    elif delete_student_number not in new_student_file:  # If it's not in the new_student_file, then it was deleted
        return True
    else:  # Else it wasn't deleted as the student number wasn't found
        return False


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


def file_write(new_student):
    with open("students.txt", 'a') as file_object:
        file_object.write(str(new_student))


def add_grade():
    student_number = input("Enter the student number: ")
    with open("students.txt", "r") as file_object:  # Have to read, and THEN write after. I tried "r+" but didn't work
        student_file = file_object.readlines()  # Create a list of each line as a string
    with open("students.txt", "w") as file_object:
        for line in student_file:
            student_tokens = line.split()  # Create a list, add to list, make it into a string, write it
            if student_number in line:  # If the line doesn't contain the student number, then rewrite it
                student_grade = input("Enter the new grade you wish to add: ")
                student_tokens.append(student_grade)
                file_object.write(" ".join(student_tokens) + "\n")
            else:
                file_object.write(line)


def calculate_class_average():
    student_list = file_read()  # Returns a list of student objects
    class_gpa = 0  # Acts as a counter to add student GPAs to
    students_with_gpa = 0  # Acts as a counter to count how many students have grades
    for student in student_list:
        print(student.get_first_name(), student.get_last_name() + "'s GPA is:", student.get_gpa())
        if student.get_gpa() is not None:  # get_gpa() will return None if student object has no grades
            class_gpa += student.get_gpa()  # Add the GPA of each student with a GPA to class_gpa
            students_with_gpa += 1  # Add 1 to students_with_gpa
    print("The class average is:", round(class_gpa / students_with_gpa, 2))  # Only counts students with a GPA


def print_class_list():
    student_list = file_read()  # Returns a list of student objects
    sorting_list = []  # Create empty list for sorting purposes
    for student in student_list:
        # Append a list to sorting_list in the form of [last_name, StudentObject]
        sorting_list.append([student.get_last_name(), student])
    sorting_list.sort()  # Sort the sorting_list alphabetically
    for student in sorting_list:  # sorting_list now sorted, loop through list and print info of each student
        student[1].print_info()


def main():
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
            delete_student_number = input("What is the student number that you wish to delete? ")
            delete_result = file_delete_student(delete_student_number)
            if delete_result is True:
                print("The student was deleted.")
            else:
                print("Student number was not found. The student was not deleted.")
        elif choice == "3":
            calculate_class_average()
        elif choice == "4":
            print_class_list()
        elif choice == "5":
            add_grade()
        elif choice == "6":
            break
        else:
            print("You did not enter a valid input. Please enter a valid input.")


if __name__ == '__main__':
    main()
