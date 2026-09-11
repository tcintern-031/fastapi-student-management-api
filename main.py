from fastapi import FastAPI, HTTPException
from model import students
from models import Student

app = FastAPI()


@app.get("/")
def greet():
    return( "I am hafiz hamza")

@app.get("/students")
def get_all_students():
    return students

@app.get("/students/search")
def search_student(name:str):
    results = []
    for student in students:
        if student["name"] == name:
           results.append(student)
    return results


@app.get("/students/{id}")
def student_by_id(id: int):
    for student in students:
        if student["id"] == id:
            return student
    raise HTTPException(
        status_code=404,
        detail= "student not found"
    )

@app.post("/students" , status_code=201)
def post_student_data(student: Student):
    students.append(student.model_dump())
    return student

@app.put("/students/{id}")
def update_student_data(id:int, student_data:Student):
    for index, student in enumerate(students):
        if student["id"] == id:
            students[index] = student_data.model_dump()
            return student_data
    raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


@app.delete("/students/{id}")
def delete_Student_Data(id:int):
    for index, student in enumerate(students):
        if student["id"] == id:
            delete_Student = students.pop(index)
            return delete_Student
    raise HTTPException(
         status_code = 404,
         detail="Student not found"
    )