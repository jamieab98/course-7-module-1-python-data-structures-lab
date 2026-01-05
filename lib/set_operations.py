# This module contains operations related to sets.
from student_data import students

def unique_majors(student_list):
    unique = {major[2] for major in student_list}
    print(unique)
    return(unique)
    
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    pass

unique_majors(students)