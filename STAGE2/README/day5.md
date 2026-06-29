# 📚 Stage 2 - Day 5
# FastAPI Request Model, Response Model & Error Handling

> Road to 100 Juta 🚀
>
> Learning Path: Backend Engineering with FastAPI

---

# 🎯 Tujuan Pembelajaran

Pada Day 5 saya mempelajari bagaimana FastAPI menangani:

- Request Model
- Response Model
- HTTPException
- Custom Exception Handler
- Pydantic Validation
- Type Coercion
- API Contract
- Error Handling Architecture

Fokus utama hari ini bukan hanya membuat endpoint berjalan, tetapi memahami **bagaimana alur data bekerja di dalam FastAPI**.

---

# 📖 Materi yang Dipelajari

## 1. Request Model

### Konsep

Request Model digunakan untuk memvalidasi data yang dikirim client sebelum masuk ke Business Logic.

Menggunakan:

```python
class Student(BaseModel):
    name: str
    age: int
    email: EmailStr
```

### Alur

```
Client

↓

Request Body

↓

Pydantic Validation

↓

Business Logic

↓

Response
```

### Hal yang dipelajari

- BaseModel
- EmailStr
- Type Validation
- Request Body
- HTTP 422 Validation Error

---

## 2. Response Model

### Konsep

Response Model digunakan untuk memfilter data yang dikirim kembali ke client.

Contoh:

```python
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
```

Endpoint

```python
@app.get("/user", response_model=UserResponse)
```

### Yang dipelajari

Response Model:

✅ Tidak mengubah object asli

✅ Hanya memfilter data yang dikirim ke client

Business Logic tetap dapat menggunakan seluruh field.

---

## Contoh

Object asli

```python
User(
    id=1,
    name="Naufal",
    email="naufal@gmail.com",
    password_hash="xxxx",
    role="admin"
)
```

Client menerima

```json
{
    "id":1,
    "name":"Naufal",
    "email":"naufal@gmail.com"
}
```

---

# 3. Error Handling

## Validation Error (422)

Terjadi sebelum endpoint dijalankan.

Contoh

```json
{
    "age":"dua puluh"
}
```

↓

422 Validation Error

Ditangani oleh

- FastAPI
- Pydantic

---

## Business Error

Terjadi ketika Business Logic berjalan.

Contoh

Student tidak ditemukan.

```python
raise HTTPException(
    status_code=404,
    detail="Student tidak ditemukan"
)
```

---

# 4. HTTPException

Digunakan untuk mengirim status code HTTP kepada client.

Contoh

```python
raise HTTPException(
    status_code=404,
    detail="Student tidak ditemukan"
)
```

Perbedaan

❌

```python
return {
    "error":"Student tidak ditemukan"
}
```

Status

```
200 OK
```

✅

```python
raise HTTPException(...)
```

Status

```
404 Not Found
```

---

# 5. Custom Exception Handler

Digunakan agar seluruh endpoint memiliki format error yang konsisten.

```python
@app.exception_handler(HTTPException)
```

Output

```json
{
    "success": false,
    "data": null,
    "message": "Student tidak ditemukan",
    "error_code": 404
}
```

---

# 6. Type Coercion

Pydantic dapat mengubah tipe data apabila masih aman.

Contoh

Input

```json
{
    "age":"20"
}
```

↓

Output

```python
age = 20
```

Namun

```json
{
    "age":"dua puluh"
}
```

↓

422 Validation Error

---

# 7. Default Value

Contoh

```python
class Student(BaseModel):
    age: int = 18
```

Jika client tidak mengirim age

↓

```python
age = 18
```

Namun jika client mengirim

```json
{
    "age": null
}
```

↓

422 Validation Error

---

# Arsitektur FastAPI

```
             CLIENT

                │

        Request JSON

                │

                ▼

        Request Model

                │

                ▼

        Business Logic

                │

                ▼

      Response Model

                │

                ▼

        Response JSON

                │

                ▼

              CLIENT
```

---

# Error Flow

```
Client

↓

Request

↓

Pydantic Validation

↓

422 (Jika Schema Salah)

↓

Business Logic

↓

404 / 403 / 400

↓

Exception Handler

↓

JSONResponse
```

---

# Insight yang Didapat

Selama pembelajaran saya memahami bahwa:

- Request Model bertugas memvalidasi data yang masuk.
- Response Model bertugas memfilter data yang keluar.
- Object backend tidak berubah ketika menggunakan Response Model.
- HTTPException digunakan untuk mengirim status code HTTP yang benar.
- Exception Handler membuat format error menjadi konsisten.
- Pydantic melakukan validasi sekaligus type coercion jika memungkinkan.
- API Contract memisahkan Request, Business Logic, dan Response.

---

# Tools

- Python
- FastAPI
- Uvicorn
- Pydantic
- Swagger UI

---

# Hasil Pembelajaran

✅ Memahami Request Model

✅ Memahami Response Model

✅ Memahami HTTPException

✅ Memahami Custom Exception Handler

✅ Memahami Type Validation

✅ Memahami Type Coercion

✅ Memahami Error Handling

✅ Memahami API Contract

---

# Progress

Stage 2

```
Day 1  ✅
Day 2  ✅
Day 3  ✅
Day 4  ✅
Day 5  ✅
```

---

# Catatan Mentor

Materi Day 5 mengubah cara berpikir dari sekadar membuat endpoint menjadi memahami bagaimana FastAPI mengelola alur request, validasi, business logic, response, dan error handling. Fokus utama bukan menghafal sintaks, tetapi memahami arsitektur yang digunakan pada backend modern.