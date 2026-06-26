# 📚 Day 4 - Stage 2

# FastAPI Fundamental (Deep Work 1 & Deep Work 2)


**Author:** Naufalz
**Stage:** Stage 2
**Day:** 4
**Topik:** FastAPI Fundamental, REST API, Parameter Binding, Request Body & Pydantic

---

# 🎯 Tujuan Pembelajaran

Pada sesi ini saya mempelajari dasar arsitektur FastAPI yang digunakan dalam pengembangan REST API modern.

Materi difokuskan pada bagaimana FastAPI menerima request dari client, melakukan proses binding, validasi menggunakan Pydantic, hingga akhirnya menjalankan Business Logic.

---

# 📖 Deep Work 1

## 1. REST API

REST (Representational State Transfer) adalah standar komunikasi antara Client dan Server menggunakan protokol HTTP.

REST menggunakan beberapa HTTP Method sesuai tujuan request.

| Method | Fungsi                 |
| ------ | ---------------------- |
| GET    | Mengambil data         |
| POST   | Menambahkan data       |
| PUT    | Mengganti seluruh data |
| PATCH  | Mengubah sebagian data |
| DELETE | Menghapus data         |

---

# 2. Route vs Endpoint

### Route

Merupakan alamat/path yang dikenali oleh server.

Contoh:

```text
/users
```

### Endpoint

Endpoint merupakan kombinasi antara HTTP Method dan Route.

Contoh:

```http
GET /users
POST /users
DELETE /users/10
```

Walaupun route sama, endpoint dapat berbeda karena HTTP Method berbeda.

---

# 3. Path Parameter

Digunakan untuk mengambil resource tertentu berdasarkan identitasnya.

Contoh:

```http
GET /users/10
```

IPO

| Input         | Process            | Output      |
| ------------- | ------------------ | ----------- |
| GET /users/10 | Mencari user id 10 | Detail user |

---

# 4. Query Parameter

Digunakan untuk filtering, searching, sorting, pagination.

Contoh:

```http
GET /products?category=laptop&limit=5
```

IPO

| Input           | Process              | Output          |
| --------------- | -------------------- | --------------- |
| category=laptop | Filter kategori      | Produk laptop   |
| limit=5         | Ambil 5 data pertama | Maksimal 5 data |

---

# 5. Request Body

Digunakan pada HTTP Method seperti POST, PUT, dan PATCH untuk mengirim data.

Contoh JSON

```json
{
    "name":"Oberon",
    "email":"oberon@mail.com",
    "age":20
}
```

Request Body lebih cocok dibanding Query Parameter karena:

* Struktur lebih jelas
* Dapat mengirim data kompleks
* Lebih mudah divalidasi
* Tidak membuat URL panjang

---

# 6. Pydantic

Pydantic digunakan untuk:

* Validasi data
* Type Conversion
* Membuat Object Python dari JSON
* Menolak Request yang tidak valid

Contoh

```python
class User(BaseModel):
    name: str
    email: str
    age: int
```

---

# Arsitektur FastAPI

```text
Client
    │
    ▼
HTTP Request
    │
    ▼
FastAPI
(Route & Binding)
    │
    ▼
Pydantic
(Validation & Type Conversion)
    │
    ▼
Business Logic
    │
    ▼
HTTP Response
```

---

# 📖 Deep Work 2

## 1. Membuat Aplikasi FastAPI

```python
from fastapi import FastAPI

app = FastAPI()
```

FastAPI membuat object aplikasi yang nantinya digunakan untuk mendaftarkan endpoint.

---

## 2. Membuat Endpoint

```python
@app.get("/")
def home():
    return {
        "message":"Hello"
    }
```

Flow

```text
Browser

↓

GET /

↓

Router

↓

home()

↓

Return Dictionary

↓

JSON Response
```

---

## 3. Path Parameter

```python
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {
        "user_id":user_id
    }
```

Request

```http
GET /users/10
```

Response

```json
{
    "user_id":10
}
```

FastAPI mengambil data dari URL Path kemudian Pydantic mengubah string menjadi integer.

---

## 4. Query Parameter

```python
@app.get("/products")
def get_products(
    category:str,
    limit:int
):
    return {
        "category":category,
        "limit":limit
    }
```

Request

```http
GET /products?category=laptop&limit=5
```

Response

```json
{
    "category":"laptop",
    "limit":5
}
```

---

## 5. Default Query Parameter

```python
@app.get("/search")
def search(
    keyword:str,
    page:int=1
):
    return {
        "keyword":keyword,
        "page":page
    }
```

Jika client tidak mengirim parameter page maka FastAPI menggunakan nilai default yaitu 1.

---

## 6. POST Endpoint

```python
@app.post("/users")
def create_user():
    return {
        "message":"User berhasil dibuat"
    }
```

Endpoint di atas hanya mengembalikan response dan belum menerima data dari client.

---

## 7. BaseModel

```python
from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    age:int
```

BaseModel berfungsi sebagai blueprint data sekaligus validator.

---

## 8. Request Body Binding

```python
@app.post("/users")
def create_user(user:User):

    return {
        "message":"User berhasil dibuat"
    }
```

FastAPI secara otomatis:

1. Mengambil JSON Body
2. Membuat Object User
3. Melakukan Validasi
4. Mengirim Object User ke Function

Flow

```text
JSON Body

↓

FastAPI

↓

Pydantic

↓

Object User

↓

create_user(user)
```

---

## 9. Validation

Contoh Request Valid

```json
{
    "name":"Oberon",
    "email":"oberon@mail.com",
    "age":20
}
```

Contoh Request Tidak Valid

```json
{
    "name":"Oberon",
    "email":"oberon@mail.com",
    "age":"abc"
}
```

Hasil

```http
422 Unprocessable Entity
```

Business Logic tidak dijalankan karena request dihentikan oleh Pydantic.

---

# 🔥 Konsep Penting yang Dipelajari

## FastAPI

Bertugas:

* Router
* Endpoint
* Binding Data
* Mengirim Response

## Pydantic

Bertugas:

* Validasi
* Type Conversion
* Membuat Object Python
* Menolak Request Tidak Valid

---

# Ringkasan Parameter Binding

| Jenis Data      | FastAPI Mengambil Dari | Pydantic Mengubah Menjadi  |
| --------------- | ---------------------- | -------------------------- |
| Path Parameter  | URL Path               | Integer / Boolean / String |
| Query Parameter | Query String           | Integer / Boolean / String |
| Request Body    | JSON Body              | Object BaseModel           |

---

# Insight Hari Ini

Seluruh mekanisme FastAPI sebenarnya mengikuti satu pipeline yang sama.

```text
HTTP Request
      │
      ▼
FastAPI
      │
      ▼
Parameter Binding
      │
      ▼
Type Conversion
      │
      ▼
Validation
      │
      ▼
Business Logic
      │
      ▼
HTTP Response
```

Yang membedakan hanya sumber datanya:

* URL Path
* Query String
* JSON Body

Sedangkan proses Binding, Validation, dan Business Logic selalu sama.

---

# 📌 Hasil Pembelajaran

Pada akhir Day 4 saya mampu memahami:

* Konsep REST API
* Route dan Endpoint
* HTTP Method
* Path Parameter
* Query Parameter
* Request Body
* Type Hint
* FastAPI Router
* Parameter Binding
* Pydantic Validation
* BaseModel
* Automatic Type Conversion
* Validation Boundary
* Hubungan antara FastAPI dan Pydantic dalam arsitektur backend modern.
