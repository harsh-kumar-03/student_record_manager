# Student Record Manager

A Django web application for managing student records with custom sorting algorithms and search functionality.

## Features

- **CRUD Operations**: Add, view, update, and delete student records
- **Student Information**: Name, roll number, and marks (0-100)
- **Custom Sorting**: 
  - Sort by name using Bubble Sort or Insertion Sort
  - Sort by marks using Bubble Sort or Insertion Sort
- **Search Functionality**: Linear search to find students by roll number
- **Responsive Design**: Clean and modern UI using Bootstrap 5
- **Grade Calculation**: Automatic grade assignment based on marks
- **Data Validation**: Form validation and unique roll number constraint

## Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Icons**: Font Awesome 6
- **Python**: 3.x

## Installation and Setup

### Prerequisites

- Python 3.x installed
- pip package manager

### Steps

1. **Clone or Download the Project**
   ```bash
   cd student_record_manager
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Adding Students
1. Click "Add Student" button
2. Fill in the form with name, roll number, and marks
3. Submit the form

### Viewing Students
- The main page displays all students in a table
- Click the eye icon to view detailed information about a student

### Editing Students
- Click the edit icon in the actions column
- Modify the information and save

### Deleting Students
- Click the delete icon in the actions column
- Confirm the deletion

### Sorting Students
- Use the sort buttons to sort by name or marks
- Choose between Bubble Sort and Insertion Sort algorithms
- The current sorting method is displayed in the stats section

### Searching Students
- Use the search form to find a student by roll number
- The system uses linear search algorithm
- Search results are displayed immediately

## Custom Algorithms

### Sorting Algorithms

#### Bubble Sort
- **By Name**: Sorts students alphabetically by name
- **By Marks**: Sorts students by marks in descending order
- Time Complexity: O(n²)

#### Insertion Sort
- **By Name**: Sorts students alphabetically by name
- **By Marks**: Sorts students by marks in descending order
- Time Complexity: O(n²)

### Search Algorithm

#### Linear Search
- Searches for a student by roll number
- Time Complexity: O(n)

## File Structure

```
student_record_manager/
├── manage.py
├── requirements.txt
├── README.md
├── student_record_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── students/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── students/
│       ├── student_list.html
│       ├── add_student.html
│       ├── edit_student.html
│       ├── delete_student.html
│       └── student_detail.html
└── static/
    └── css/
        └── style.css
```

## Testing

Run the test suite:
```bash
python manage.py test
```

## Grade System

- **A+ (90-100)**: Excellent
- **A (80-89)**: Very Good
- **B (70-79)**: Good
- **C (60-69)**: Average
- **F (0-59)**: Fail

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is for educational purposes.

## Contact

For any questions or issues, please contact the developer.
