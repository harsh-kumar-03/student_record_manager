def bubble_sort_by_name(students):
    """
    Sort students by name using bubble sort algorithm
    """
    students_list = list(students)
    n = len(students_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if students_list[j].name.lower() > students_list[j + 1].name.lower():
                students_list[j], students_list[j + 1] = students_list[j + 1], students_list[j]
    
    return students_list


def bubble_sort_by_marks(students):
    """
    Sort students by marks using bubble sort algorithm (descending order)
    """
    students_list = list(students)
    n = len(students_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if students_list[j].marks < students_list[j + 1].marks:
                students_list[j], students_list[j + 1] = students_list[j + 1], students_list[j]
    
    return students_list


def insertion_sort_by_name(students):
    """
    Sort students by name using insertion sort algorithm
    """
    students_list = list(students)
    
    for i in range(1, len(students_list)):
        key = students_list[i]
        j = i - 1
        
        while j >= 0 and students_list[j].name.lower() > key.name.lower():
            students_list[j + 1] = students_list[j]
            j -= 1
        
        students_list[j + 1] = key
    
    return students_list


def insertion_sort_by_marks(students):
    """
    Sort students by marks using insertion sort algorithm (descending order)
    """
    students_list = list(students)
    
    for i in range(1, len(students_list)):
        key = students_list[i]
        j = i - 1
        
        while j >= 0 and students_list[j].marks < key.marks:
            students_list[j + 1] = students_list[j]
            j -= 1
        
        students_list[j + 1] = key
    
    return students_list


def linear_search_by_roll_number(students, roll_number):
    """
    Search for a student by roll number using linear search algorithm
    """
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None
