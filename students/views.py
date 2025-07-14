from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Student
from .forms import StudentForm, SearchForm
from .utils import (
    bubble_sort_by_name, bubble_sort_by_marks,
    insertion_sort_by_name, insertion_sort_by_marks,
    linear_search_by_roll_number
)


def student_list(request):
    """
    Display list of all students with sorting and searching functionality
    """
    students = Student.objects.all()
    search_form = SearchForm()
    search_result = None
    
    # Handle search
    if request.method == 'POST' and 'search' in request.POST:
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            roll_number = search_form.cleaned_data['roll_number']
            search_result = linear_search_by_roll_number(students, roll_number)
            if not search_result:
                messages.warning(request, f"No student found with roll number: {roll_number}")
    
    # Handle sorting
    sort_by = request.GET.get('sort_by', 'default')
    algorithm = request.GET.get('algorithm', 'bubble')
    
    if sort_by == 'name':
        if algorithm == 'bubble':
            students = bubble_sort_by_name(students)
        else:
            students = insertion_sort_by_name(students)
    elif sort_by == 'marks':
        if algorithm == 'bubble':
            students = bubble_sort_by_marks(students)
        else:
            students = insertion_sort_by_marks(students)
    else:
        students = list(students)
    
    context = {
        'students': students,
        'search_form': search_form,
        'search_result': search_result,
        'current_sort': sort_by,
        'current_algorithm': algorithm,
    }
    
    return render(request, 'students/student_list.html', context)


def add_student(request):
    """
    Add a new student record
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                student = form.save()
                messages.success(request, f'Student "{student.name}" added successfully!')
                return redirect('student_list')
            except IntegrityError:
                messages.error(request, 'A student with this roll number already exists.')
    else:
        form = StudentForm()
    
    return render(request, 'students/add_student.html', {'form': form})


def edit_student(request, pk):
    """
    Edit an existing student record
    """
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            try:
                student = form.save()
                messages.success(request, f'Student "{student.name}" updated successfully!')
                return redirect('student_list')
            except IntegrityError:
                messages.error(request, 'A student with this roll number already exists.')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})


def delete_student(request, pk):
    """
    Delete a student record
    """
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f'Student "{student_name}" deleted successfully!')
        return redirect('student_list')
    
    return render(request, 'students/delete_student.html', {'student': student})


def student_detail(request, pk):
    """
    Display detailed view of a student
    """
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
