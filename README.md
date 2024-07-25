# Django Project Setup Guide

## Overview

This project is a web application built using Python with the Django framework. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `venv` (Python virtual environment module)

## Setting Up the Project

### Windows

1. **Clone the Repository**

   ```bash
   git clone https://github.com/andrea-chirillano/userpilot.git
   cd userpilot
Create a Virtual Environment

2. **Activate the Virtual Environment**

   ```bash
    python -m venv venv

3. **Install Dependencies**

   ```bash
    venv\Scripts\activate

4. **Run Migrations**
   ```bash
    pip install -r requirements.txt

5. **Create a Superuser**
   ```bash
    python manage.py migrate

6. **Follow the prompts to create an admin user.**
   ```bash
    python manage.py createsuperuser

Run the Development Server

7. **Access the Application**
   ```bash
    python manage.py runserver

Visit http://127.0.0.1:8000/ to view the application.
Visit http://127.0.0.1:8000/admin/ to access the Django admin interface.



### Linux
1. **Clone the Repository**
    ```bash
    git clone https://github.com/andrea-chirillano/userpilot.git
    cd userpilot
Create a Virtual Environment

2. **Activate the Virtual Environment**
   ```bash
    python3 -m venv venv

3. **Install Dependencies**
   ```bash
    source venv/bin/activate

4. **Run Migrations**
   ```bash
    pip install -r requirements.txt

5. **Create a Superuser**
   ```bash
    python manage.py migrate

6. **Follow the prompts to create an admin user.**
    ```bash
    python manage.py createsuperuser

Run the Development Server

7. Access the Application
     ```bash
    python manage.py runserver

Visit http://127.0.0.1:8000/ to view the application.
Visit http://127.0.0.1:8000/admin/ to access the Django admin interface.
