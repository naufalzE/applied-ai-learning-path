from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Stage 2 Day 5 - FastAPI",
    version="1.0.0"
)

# =====================================================
# REQUEST MODEL
# =====================================================

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr


# =====================================================
# RESPONSE MODEL
# =====================================================

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password_hash: str
    role: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


# =====================================================
# DUMMY DATABASE
# =====================================================

students = {
    1: "Naufal",
    2: "Budi",
    3: "Andi"
}


# =====================================================
# CUSTOM EXCEPTION HANDLER
# =====================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Semua HTTPException akan masuk ke sini.
    Tujuannya agar format error konsisten.
    """

    return JSONResponse(
        status_code=exc.status_code,      # HTTP Status Code
        content={
            "success": False,
            "data": None,
            "message": exc.detail,
            "error_code": exc.status_code
        }
    )


# =====================================================
# POST : REQUEST MODEL
# =====================================================

@app.post("/students")
def create_student(student: Student):
    """
    Menerima Request Body.
    Pydantic otomatis melakukan validasi.
    """

    print(type(student))
    print(student.name)
    print(student.age)
    print(student.email)

    return student


# =====================================================
# GET : RESPONSE MODEL
# =====================================================

@app.get("/user", response_model=UserResponse)
def get_user():

    user = User(
        id=1,
        name="Naufal",
        email="naufal@gmail.com",
        password_hash="$2b$12$abcd123456",
        role="admin"
    )

    # Business Logic masih bisa memakai seluruh data
    print(user.password_hash)
    print(user.role)

    return user


# =====================================================
# GET : HTTPException
# =====================================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:

        raise HTTPException(
            status_code=404,
            detail="Student tidak ditemukan"
        )

    return {
        "id": student_id,
        "name": students[student_id]
    }