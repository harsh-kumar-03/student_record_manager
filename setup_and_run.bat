@echo off
echo ================================
echo  Student Record Manager Setup
echo ================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.x from https://python.org
    pause
    exit /b 1
)

echo Python is installed.
echo.

echo Installing Django and dependencies...
pip install Django==4.2.7
if %errorlevel% neq 0 (
    echo ERROR: Failed to install Django
    pause
    exit /b 1
)

echo.
echo Creating database and running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo Would you like to create a superuser account? (y/n)
set /p create_superuser=
if /i "%create_superuser%"=="y" (
    echo Creating superuser...
    python manage.py createsuperuser
)

echo.
echo Setup complete!
echo.
echo Starting the development server...
echo Open your browser and go to: http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver
