from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.post("/students")
def create_student(student: Student):
    print(type(student))
    print(student.name)
    print(student.age)
    print(student.email)

    return student