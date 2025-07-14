from django.test import TestCase
from django.urls import reverse
from .models import Student
from .utils import (
    bubble_sort_by_name, bubble_sort_by_marks,
    insertion_sort_by_name, insertion_sort_by_marks,
    linear_search_by_roll_number
)


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            roll_number="CS001",
            marks=85
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.roll_number, "CS001")
        self.assertEqual(self.student.marks, 85)

    def test_student_str_method(self):
        self.assertEqual(str(self.student), "John Doe - CS001")


class SortingAlgorithmTest(TestCase):
    def setUp(self):
        self.students = [
            Student.objects.create(name="Charlie", roll_number="CS003", marks=78),
            Student.objects.create(name="Alice", roll_number="CS001", marks=92),
            Student.objects.create(name="Bob", roll_number="CS002", marks=85),
        ]

    def test_bubble_sort_by_name(self):
        sorted_students = bubble_sort_by_name(self.students)
        names = [student.name for student in sorted_students]
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])

    def test_bubble_sort_by_marks(self):
        sorted_students = bubble_sort_by_marks(self.students)
        marks = [student.marks for student in sorted_students]
        self.assertEqual(marks, [92, 85, 78])

    def test_insertion_sort_by_name(self):
        sorted_students = insertion_sort_by_name(self.students)
        names = [student.name for student in sorted_students]
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])

    def test_insertion_sort_by_marks(self):
        sorted_students = insertion_sort_by_marks(self.students)
        marks = [student.marks for student in sorted_students]
        self.assertEqual(marks, [92, 85, 78])


class SearchAlgorithmTest(TestCase):
    def setUp(self):
        self.students = [
            Student.objects.create(name="Alice", roll_number="CS001", marks=92),
            Student.objects.create(name="Bob", roll_number="CS002", marks=85),
            Student.objects.create(name="Charlie", roll_number="CS003", marks=78),
        ]

    def test_linear_search_found(self):
        result = linear_search_by_roll_number(self.students, "CS002")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Bob")

    def test_linear_search_not_found(self):
        result = linear_search_by_roll_number(self.students, "CS999")
        self.assertIsNone(result)


class StudentViewTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Test Student",
            roll_number="TEST001",
            marks=90
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Student")

    def test_add_student_view(self):
        response = self.client.get(reverse('add_student'))
        self.assertEqual(response.status_code, 200)

    def test_edit_student_view(self):
        response = self.client.get(reverse('edit_student', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_student_view(self):
        response = self.client.get(reverse('delete_student', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
