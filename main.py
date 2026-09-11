from fastapi import FastAPI, HTTPException
from model import students
from pydantic import BaseModel


app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    age:int

@app.get("/")
def greet():
    return( "I am hafiz hamza")

@app.get("/students")
def get_all_students():
    return students

@app.get("/students/{id}")
def student_by_id(id: int):
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(
        status_code=404,
        detail= "student not found"
    )

@app.post("/students")
def post_student_data(student: Student):
    students.append(student.model_dump())
    return student

@app.put("/students/{id}")
def update_student_data(id:int, student_data:Student):
    for index ,student in enumerate(students):
        if student["id"] == id:
            students[index]=student_data.model_dump()
            return student[index]
            
    raise HTTPException(
        status_code = 404,
        detail="student not found"
        )

@app.delete("/students/{id}")
def delete_student_data(id:int):
    for index, student in enumerate(students):
        if student["id"] == id:
            delete_student = students.pop(index)
            return delete_student

    raise HTTPException(
        status_code = 404,
        detail="Student not found"
    )
