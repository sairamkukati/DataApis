
# Project: DataApis

This is a Django project for managing and accessing various APIs. The project provides a simple interface for interacting with database models via RESTful endpoints.

## Setup Instructions

### Prerequisites
- Python (version 3.8 or higher)
- pip (Python package manager)
- Git
- A virtual environment tool (optional but recommended)

### Steps to Set Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sairamkukati/DataApis.git
   cd DataApis
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database**:
   - Run migrations to create the database structure:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

   The server will start at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Documentation

You can view the Swagger API documentation at:
[http://127.0.0.1:8000/swagger-api/](http://127.0.0.1:8000/swagger-api/)

This provides an interactive interface to test and explore the available endpoints.
