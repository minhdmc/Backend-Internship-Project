# Employee Management System

This project is a Django-based application designed to manage employee-related data and provide analytics through a RESTful API and visualizations.

## Features

- Employee management with CRUD operations
- Department management
- Attendance tracking
- Performance evaluation
- API endpoints for accessing employee data
- Analytics dashboard with visualizations

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL (or any other database of your choice)
- HTML/CSS/JavaScript for front-end
- Chart.js for data visualization

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd employee_management_system
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Update the `DATABASES` setting in `employee_management_system/settings.py` with your database configuration.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. **Seed the database with dummy data:**
   - Create a management command or use Django shell to add dummy employee data.

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the API:**
   - The API endpoints are defined in `employee_api/urls.py`. You can access them at `http://127.0.0.1:8000/api/`.

8. **Access the analytics dashboard:**
   - The dashboard can be accessed at `http://127.0.0.1:8000/analytics/`.

## API Endpoints

- `GET /api/employees/` - List all employees
- `POST /api/employees/` - Create a new employee
- `GET /api/employees/{id}/` - Retrieve a specific employee
- `PUT /api/employees/{id}/` - Update a specific employee
- `DELETE /api/employees/{id}/` - Delete a specific employee

## License

This project is licensed under the MIT License. See the LICENSE file for details.