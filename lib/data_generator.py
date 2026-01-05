# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    student_records = (record for record in student_list if record[2].lower() == major.lower())
    for record in student_records:
        print(record)

    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    pass
