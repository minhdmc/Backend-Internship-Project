# Employee Management System

A Django-based Employee Management System with RESTful APIs and analytics capabilities.

## Features

- Employee management (CRUD operations)
- Department management
- Attendance tracking
- Performance reviews
- RESTful APIs with Swagger documentation
- Data visualization (optional)
- Authentication and authorization

## Tech Stack

- Django 4.2
- Django REST Framework
- PostgreSQL (configurable)
- Swagger/OpenAPI documentation
- Chart.js for visualizations

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- PostgreSQL (optional, SQLite is used by default)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd employee_management_system
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file in the project root
cp .env.example .env

# Edit .env with your configuration
# Example .env contents:
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:password@localhost:5432/employee_db
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
# Follow the prompts to create an admin user
```

7. Seed the database with sample data:
```bash
python manage.py seed_data
```

8. Run the development server:
```bash
python manage.py runserver
```

## Accessing the Application

Once the server is running, you can access:

1. Admin Interface:
   - URL: http://localhost:8000/admin/
   - Login with your superuser credentials
   - Manage all data through the Django admin interface

2. API Documentation:
   - Swagger UI: http://localhost:8000/swagger/
   - ReDoc: http://localhost:8000/redoc/
   - Interactive API documentation and testing

3. Analytics Dashboard:
   - URL: http://localhost:8000/analytics/dashboard/
   - View employee statistics and charts

## API Endpoints

### Department Management
- `GET /api/departments/` - List all departments
- `POST /api/departments/` - Create a new department
- `GET /api/departments/{id}/` - Retrieve a specific department
- `PUT /api/departments/{id}/` - Update a department
- `DELETE /api/departments/{id}/` - Delete a department

### Employee Management
- `GET /api/employees/` - List all employees
- `POST /api/employees/` - Create a new employee
- `GET /api/employees/{id}/` - Retrieve a specific employee
- `PUT /api/employees/{id}/` - Update an employee
- `DELETE /api/employees/{id}/` - Delete an employee

### Attendance Tracking
- `GET /api/attendance/` - List all attendance records
- `POST /api/attendance/` - Create a new attendance record
- `GET /api/attendance/{id}/` - Retrieve a specific attendance record
- `PUT /api/attendance/{id}/` - Update an attendance record
- `DELETE /api/attendance/{id}/` - Delete an attendance record

### Performance Reviews
- `GET /api/performance/` - List all performance reviews
- `POST /api/performance/` - Create a new performance review
- `GET /api/performance/{id}/` - Retrieve a specific performance review
- `PUT /api/performance/{id}/` - Update a performance review
- `DELETE /api/performance/{id}/` - Delete a performance review

## API Usage Examples

### Authentication
```bash
# Get authentication token
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'

# Use token in subsequent requests
curl http://localhost:8000/api/employees/ \
     -H "Authorization: Token your_token_here"
```

### Creating an Employee
```bash
curl -X POST http://localhost:8000/api/employees/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token your_token_here" \
     -d '{
           "first_name": "John",
           "last_name": "Doe",
           "email": "john.doe@example.com",
           "phone_number": "+1234567890",
           "address": "123 Main St",
           "department": 1,
           "date_of_birth": "1990-01-01",
           "date_hired": "2023-01-01"
         }'
```

### Recording Attendance
```bash
curl -X POST http://localhost:8000/api/attendance/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token your_token_here" \
     -d '{
           "employee": 1,
           "date": "2024-01-20",
           "status": "PRESENT",
           "check_in": "09:00:00",
           "check_out": "17:00:00"
         }'
```

## Features in Detail

### Employee Management
- Create, read, update, and delete employee records
- Track employee details (name, email, phone, address)
- Associate employees with departments
- Filter and search employees by various criteria

### Department Management
- Create and manage departments
- View department-wise employee distribution
- Track department performance metrics

### Attendance Tracking
- Record daily attendance
- Track attendance status (Present/Absent/Late)
- Generate attendance reports
- Monitor attendance patterns

### Performance Reviews
- Record performance ratings (1-5)
- Add review comments and goals
- Track improvement areas
- Generate performance reports

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
The project follows PEP 8 style guide. To check your code:
```bash
# Install flake8
pip install flake8

# Run flake8
flake8 .
```

### Database Management
```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (if needed)
python manage.py flush
```

## Troubleshooting

### Common Issues

1. Database Connection Issues
   - Check your database settings in settings.py
   - Ensure PostgreSQL is running (if using PostgreSQL)
   - Verify database credentials in .env file

2. Migration Errors
   - Delete all migration files (except __init__.py)
   - Delete the database
   - Run `python manage.py makemigrations`
   - Run `python manage.py migrate`

3. Static Files Not Loading
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings
   - Verify static files are in the correct directory

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
