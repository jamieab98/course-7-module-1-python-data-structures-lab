# This module contains functions to process student data.

def format_student_data(student):
    returned_string = f"ID: {student[0]} | Name: {student[1]} | Major: {student[1]}"
    print(returned_string)
    return(returned_string)
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
        format_student_data(student)
    return
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    pass
