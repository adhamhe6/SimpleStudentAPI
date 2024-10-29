# SimpleStudentAPI

A simple RESTful API for managing student records built with FastAPI and Pydantic. This API allows you to perform CRUD operations (Create, Read, Update, Delete) on student data.

## Features

- **Get All Students**: Retrieve a list of all students.
- **Create Student**: Add a new student to the records.
- **Update Student**: Modify existing student details.
- **Delete Student**: Remove a student from the records.
- **CORS Support**: Easily integrate with front-end applications.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or later
- FastAPI
- Pydantic

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/adhamhe6/SimpleStudentAPI.git
    cd SimpleStudentAPI
    ```

2. Install the dependencies:

    ```bash
    pip install fastapi[all]
    ```

### Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Database Setup

The API uses an SQLite database (`students.db`) for persistent storage of student records. The database is automatically created upon running the API for the first time.

### Notes:
- This updated README includes information about SQLite and SQLAlchemy, highlighting their role in the project.
- Adjust any specifics based on your implementation or additional features you might want to include!