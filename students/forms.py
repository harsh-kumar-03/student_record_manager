from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'marks']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number'
            }),
            'marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter marks (0-100)',
                'min': 0,
                'max': 100
            })
        }

    def clean_roll_number(self):
        roll_number = self.cleaned_data['roll_number']
        if Student.objects.filter(roll_number=roll_number).exists():
            if not self.instance or self.instance.roll_number != roll_number:
                raise forms.ValidationError("A student with this roll number already exists.")
        return roll_number


class SearchForm(forms.Form):
    roll_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter roll number to search'
        })
    )
