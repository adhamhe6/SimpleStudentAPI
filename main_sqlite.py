import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend's origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for Student
class Student(BaseModel):
    id: int = None
    name: str
    grade: int

# Function to set up the database
def setup_database():
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database setup error: {e}")

# Call setup_database at the start of the application
setup_database()

# Read all students
@app.get("/students/")
async def read_students():
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        # Return students as a list of dictionaries
        return [{"id": row[0], "name": row[1], "grade": row[2]} for row in rows]
    except sqlite3.Error as e:
        print(e)
        return {"error": "Failed to fetch students"}

# Create a new student
@app.post("/students/")
async def create_student(student: Student):
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (student.name, student.grade))
        conn.commit()
        student_id = cursor.lastrowid  # Get the id of the newly inserted student
        conn.close()
        return {"message": "Student added successfully", "student": {"id": student_id, "name": student.name, "grade": student.grade}}
    except sqlite3.Error as e:
        print(e)
        return {"error": "Failed to create student"}

# Update a student by ID
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        db_student = cursor.fetchone()

        if db_student is None:
            conn.close()
            raise HTTPException(status_code=404, detail="Student not found")
        
        cursor.execute("UPDATE students SET name = ?, grade = ? WHERE id = ?", (student.name, student.grade, student_id))
        conn.commit()
        conn.close()

        return {"id": student_id, "name": student.name, "grade": student.grade}
    except sqlite3.Error as e:
        print(e)
        return {"error": "Failed to update student"}

# Delete a student by ID
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        db_student = cursor.fetchone()

        if db_student is None:
            conn.close()
            raise HTTPException(status_code=404, detail="Student not found")
        
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
        
        return {"message": "Student deleted"}
    except sqlite3.Error as e:
        print(e)
        return {"error": "Failed to delete student"}
