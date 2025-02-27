# Vulnerability Management System

## Overview
The Vulnerability Management System is a backend solution for scanning and managing vulnerabilities in network infrastructure.

## Setup Instructions
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the PostgreSQL database in `settings.py`
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage
- Access the API at `http://localhost:8000/api/`
- Use the `/api/vulnerabilities/` endpoint to manage vulnerabilities.
- Use `/swagger/` for API documentation.

## Technologies
- Django, Django REST Framework
- PostgreSQL
- Nmap, OpenVAS
- JWT for Authentication
