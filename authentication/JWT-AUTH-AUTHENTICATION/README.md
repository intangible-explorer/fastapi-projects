# Basic Authentication in FastAPI

## Description
This project demonstrates basic authentication implementation using FastAPI framework. It includes user registration, login, and authenticated endpoints.

## Prerequisites
- Python 3.x
- Virtualenv (optional but recommended for isolated environment)

## Installation
1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the SQLite database:**
   ```bash
   python3 create_db.py
   ```
5. **Modify environment variables:**
   - If necessary, modify the values of environment variables in the .env file.


## Usage
1. **Import Postman Collection:**
   - Import the provided Postman collection (collection.json) into Postman to get started quickly.

2. **Run the application in dev mode:**
   ```bash
   fastapi dev app/main.py
   ```

## API Documentation
   - Once the application is running, visit http://localhost:8000/docs for the interactive API documentation provided by Swagger UI.


## Contributing
   - If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome your contributions!
