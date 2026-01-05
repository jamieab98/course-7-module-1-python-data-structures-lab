# This module contains functions to process student data.
from student_data import students

def format_student_data(selected):
    selected_student = [student for student in students if student[1].lower() == selected.lower()]
    returned_string = f"ID: {selected_student[0][0]} | Name: {selected_student[0][1]} | Major: {selected_student[0][2]}"
    print(returned_string)
    return
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    pass

def display_students(student_list):
    for student in student_list:
        student_name = student[1]
        format_student_data(student_name)
    return
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    pass

display_students(students)