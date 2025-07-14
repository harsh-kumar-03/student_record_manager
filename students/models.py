from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    marks = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.roll_number}"

    class Meta:
        ordering = ['roll_number']
