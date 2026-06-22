# Deep Work 2 - Stage 2 Day 2

## Topik

API Client dengan Python menggunakan Requests Library

---

## Tujuan Pembelajaran

Pada sesi ini mempelajari cara mengonsumsi API menggunakan Python dengan pendekatan yang digunakan pada proyek backend dan AI engineering.

Materi yang dipelajari:

* HTTP GET Request
* Response Object
* Status Code Validation
* JSON Parsing
* Error Handling
* Timeout
* ConnectionError
* Wrapper Function
* Structured Response
* JSON Schema Guard

---

# Arsitektur API Client

```text
Request
    ↓
Response
    ↓
Status Validation
    ↓
JSON Parsing
    ↓
Schema Validation
    ↓
Business Logic
```

---

# Input - Process - Output (IPO)

| Input      | Process           | Output           |
| ---------- | ----------------- | ---------------- |
| User ID    | HTTP GET Request  | Response Object  |
| Response   | Status Validation | Success / Fail   |
| JSON Data  | Schema Validation | Valid / Invalid  |
| Valid Data | Business Logic    | User Information |
| Error      | Error Handling    | Error Message    |

---

# Konsep Penting

## 1. Response Object

Ketika menggunakan:

```python
response = requests.get(url)
```

yang dikembalikan bukan JSON, melainkan Response Object.

Komponen utama:

```python
response.status_code
response.text
response.json()
```

---

## 2. Status Code Validation

Sebelum memproses data, status code harus diperiksa.

Contoh:

```python
if response.status_code == 200:
```

Status code yang dipelajari:

| Code | Arti                  |
| ---- | --------------------- |
| 200  | Success               |
| 404  | Data Tidak Ditemukan  |
| 500  | Internal Server Error |

---

## 3. JSON Parsing

Response dari API awalnya berupa string JSON.

```python
response.text
```

Untuk mengubah menjadi dictionary Python:

```python
data = response.json()
```

Contoh:

```python
{
    "name": "Leanne Graham"
}
```

---

## 4. Error Handling

### ConnectionError

Terjadi ketika server tidak dapat dihubungi.

```python
except requests.ConnectionError:
```

### Timeout

Terjadi ketika server terlalu lama merespons.

```python
except requests.Timeout:
```

---

## 5. Structured Response

Daripada hanya menggunakan:

```python
return None
```

digunakan struktur yang lebih informatif:

```python
{
    "success": True,
    "data": {...},
    "error": None
}
```

atau

```python
{
    "success": False,
    "data": None,
    "error": "Timeout"
}
```

Keuntungan:

* Informasi error lebih jelas
* Mudah di-debug
* Mudah digunakan oleh business layer

---

## 6. JSON Schema Guard

Schema guard digunakan untuk memastikan response API sesuai kontrak.

### Missing Field

```python
if "email" not in user:
```

### Null Value

```python
if user["email"] is None:
```

Schema guard dijalankan sebelum business logic.

---

# Implementasi Final

```python
import requests


def fetch_user(user_id):

    try:

        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5
        )

        if response.status_code != 200:
            return {
                "success": False,
                "data": None,
                "error": f"HTTP {response.status_code}"
            }

        user = response.json()

        required_fields = [
            "name",
            "email",
            "username"
        ]

        for field in required_fields:

            if field not in user:
                return {
                    "success": False,
                    "data": None,
                    "error": f"Missing Field: {field}"
                }

            if user[field] is None:
                return {
                    "success": False,
                    "data": None,
                    "error": f"Null Value: {field}"
                }

        return {
            "success": True,
            "data": user,
            "error": None
        }

    except requests.ConnectionError:

        return {
            "success": False,
            "data": None,
            "error": "ConnectionError"
        }

    except requests.Timeout:

        return {
            "success": False,
            "data": None,
            "error": "Timeout"
        }


result = fetch_user(1)

if result["success"]:

    user = result["data"]

    print(f"Nama     : {user['name']}")
    print(f"Email    : {user['email']}")
    print(f"Username : {user['username']}")

else:

    print("Gagal mengambil data user")
    print(f"Error : {result['error']}")
```

---

# Hasil Pembelajaran

Setelah menyelesaikan Deep Work 2 Day 2, saya memahami:

* Cara melakukan HTTP GET Request
* Cara membaca Response Object
* Cara menggunakan Status Code Validation
* Cara melakukan JSON Parsing
* Cara menangani ConnectionError dan Timeout
* Cara membuat Wrapper Function
* Cara membuat Structured Response
* Cara melakukan JSON Schema Guard
* Cara memisahkan Transport Layer, Validation Layer, dan Business Layer

---

# Progress Road to 100 Juta

Stage 2 - Day 2 ✅ Completed

Materi Selanjutnya:

* JSONDecodeError
* Generic API Wrapper
* Retry Logic
* Exponential Backoff
* Session Object
* API Client Architecture
* FastAPI Integration

```
```
# 👨‍💻 Author

**NaufalZ**
