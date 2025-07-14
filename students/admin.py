from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_number', 'marks', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'roll_number']
    ordering = ['roll_number']
    readonly_fields = ['created_at', 'updated_at']
