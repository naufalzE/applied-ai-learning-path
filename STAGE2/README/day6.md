# 📅 Deep Work 2 - Day 6
# FastAPI Project Architecture (Professional Structure)

> Road to 100 Juta 🚀
>
> Mentor: **Nexus**
>
> Fokus hari ini adalah memahami **arsitektur FastAPI** menggunakan prinsip **Separation of Concerns** dan **Single Responsibility Principle (SRP)**, bukan sekadar membuat API berjalan.

---

# 🎯 Learning Objectives

Setelah menyelesaikan Day 6, saya mampu:

- Memahami struktur project FastAPI yang scalable.
- Memahami tanggung jawab setiap folder.
- Memisahkan HTTP Layer dan Business Logic.
- Menggunakan `APIRouter`.
- Menggunakan `BaseSettings` untuk konfigurasi.
- Menggunakan `BaseModel` sebagai Request Schema.
- Membuat Service Layer.
- Menghubungkan Client → Schema → Router → Service → Response.

---

# 📂 Project Structure

```text
app/
│
├── main.py
│
├── core/
│   └── config.py
│
├── routers/
│   └── summarize.py
│
├── services/
│   └── summarize_service.py
│
└── schemas/
    └── summarize_schema.py
```

---

# 📌 Tanggung Jawab Setiap Folder

| Folder | Tanggung Jawab |
|---------|----------------|
| app | Root aplikasi |
| main.py | Entry Point & Composition Root |
| core | Konfigurasi aplikasi |
| routers | HTTP Layer |
| services | Business Logic |
| schemas | Validasi Request & Response |

---

# Kenapa Tidak Semua di main.py?

Jika semua kode ditulis di satu file:

- Sulit dibaca.
- Sulit melakukan debugging.
- Sulit melakukan testing.
- Tidak reusable.
- Business Logic bercampur dengan HTTP.

Prinsip yang digunakan:

> **Single Responsibility Principle**

Satu komponen hanya memiliki satu tanggung jawab.

---

# Entry Point

`main.py` bukan tempat membuat fitur.

`main.py` bertugas:

- Membuat aplikasi.
- Menghubungkan Router.
- Memasang Middleware.
- Menjalankan konfigurasi.

Analogi:

```
main.py
↓

Merakit aplikasi
```

---

# FastAPI Object

```python
from fastapi import FastAPI

app = FastAPI()
```

Penjelasan:

```
FastAPI (Class)

↓

app (Object)

↓

Application
```

FastAPI hanyalah blueprint.

Aplikasi baru dibuat ketika object dibuat.

---

# Config Layer

File:

```
core/config.py
```

Menggunakan:

```python
BaseSettings
```

Tujuan:

- Membaca `.env`
- Validasi konfigurasi
- Centralized Configuration

Contoh:

```python
class Settings(BaseSettings):

    llm_api_key: str

    llm_base_url: str

    timeout: int = 30

    app_name: str = "AI Assistant"

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()
```

---

# Fail Fast Principle

Konfigurasi penting dibuat Required.

Contoh:

```python
llm_api_key: str
```

Jika API Key tidak ada:

```
Application Startup

↓

Validation Error

↓

Server Stop
```

Lebih baik gagal saat startup dibanding gagal saat production.

---

# APIRouter

Router digunakan untuk mengelompokkan endpoint.

```python
router = APIRouter()
```

Router bukan aplikasi.

Router hanya kumpulan endpoint.

---

# include_router()

Pada `main.py`

```python
app.include_router(summarize_router)
```

Artinya:

```
FastAPI

↓

Mengambil semua endpoint

↓

Mendaftarkan ke Application
```

---

# Router Layer

Contoh:

```python
@router.post("/summarize")
def post_summarize():
    ...
```

Tugas Router:

- menerima HTTP Request
- validasi schema
- memanggil Service
- mengembalikan Response

Router **tidak boleh** berisi Business Logic.

---

# Service Layer

Contoh:

```python
class SummarizeService:

    def generate_summary(self, text: str):
        ...
```

Tugas Service:

- Business Logic
- AI Logic
- Database Logic
- External API

Service tidak mengetahui:

- HTTP
- FastAPI
- Request
- Response

Service hanya menerima data.

---

# Schema Layer

Menggunakan:

```python
BaseModel
```

Contoh:

```python
class SummarizeRequest(BaseModel):

    text: str
```

Tugas:

- Validasi Input
- Validasi Type
- Mengubah JSON menjadi Python Object

---

# Alur Request

```
Client

↓

JSON

↓

Schema (BaseModel)

↓

Router

↓

Service

↓

Business Logic

↓

Router

↓

JSON Response

↓

Client
```

---

# Hubungan Antar Layer

```
Client

↓

Router

↓

Service

↓

Gemini / Database
```

Router hanya menghubungkan.

Service menjalankan logika.

---

# Separation of Concerns

```
Schema

↓

Validasi


Router

↓

HTTP


Service

↓

Business Logic


Config

↓

Konfigurasi
```

Setiap layer hanya memiliki satu tanggung jawab.

---

# OOP yang Digunakan

Semua layer menggunakan pola yang sama.

```
Class

↓

Object
```

Contoh:

```python
Settings()

FastAPI()

APIRouter()

SummarizeService()
```

Semuanya adalah object.

---

# Insight Penting

## Router

Router mengetahui HTTP.

## Service

Service tidak mengetahui HTTP.

Service hanya mengetahui:

```
Input

↓

Logic

↓

Output
```

Inilah yang membuat Service reusable.

---

# Kenapa Service Tidak Mengembalikan JSON?

Karena JSON merupakan tanggung jawab Router.

Service cukup mengembalikan:

```python
str
```

atau

```python
dict
```

Router yang mengubah menjadi HTTP Response.

---

# Konsep yang Dipelajari

✅ Project Structure

✅ Entry Point

✅ Composition Root

✅ APIRouter

✅ include_router()

✅ BaseSettings

✅ SettingsConfigDict

✅ BaseModel

✅ Service Layer

✅ Request Schema

✅ Fail Fast

✅ Separation of Concerns

✅ Single Responsibility Principle

---

# Arsitektur Akhir

```
                    Client
                      │
                      ▼
              POST /summarize
                      │
                      ▼
          SummarizeRequest
            (Validation)
                      │
                      ▼
                 Router Layer
                      │
                      ▼
              SummarizeService
               (Business Logic)
                      │
                      ▼
              Gemini / Database
                      │
                      ▼
                 Router Layer
                      │
                      ▼
                JSON Response
                      │
                      ▼
                    Client
```

---

# Daily Reflection

## Pemahaman

| Materi | Nilai |
|---------|-------|
| Project Structure | 9/10 |
| Config (`BaseSettings`) | 9/10 |
| APIRouter | 9/10 |
| Service Layer | 9/10 |

---

## Hal Penting Hari Ini

Saya memahami bahwa:

- `main.py` adalah **Composition Root**, bukan tempat Business Logic.
- `Router` bertugas menangani HTTP.
- `Service` bertugas menjalankan Business Logic.
- `Schema` bertugas memvalidasi data.
- `Config` bertugas mengelola konfigurasi aplikasi.
- Setiap layer memiliki **Single Responsibility**.
- Arsitektur yang baik membuat aplikasi lebih mudah dikembangkan, diuji, dan dipelihara.

---

# Kesimpulan

Day 6 bukan tentang membuat API yang kompleks, tetapi membangun **fondasi arsitektur backend yang benar**.

Dengan memisahkan **Config**, **Schema**, **Router**, dan **Service**, aplikasi menjadi:

- Lebih bersih.
- Mudah dipelihara.
- Mudah di-debug.
- Mudah di-test.
- Mudah dikembangkan ketika project semakin besar.

Prinsip utama yang dipelajari hari ini adalah:

> **"Router mengatur lalu lintas HTTP, Service menjalankan Business Logic, Schema memvalidasi data, dan Main merakit seluruh aplikasi."**