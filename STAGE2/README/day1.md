# 🚀 Stage 2 Day 1 — Backend & API Engineering

## Road to 100 Juta

Repository dokumentasi pembelajaran **Stage 2 Day 1** yang berfokus pada fundamental Web API, HTTP, REST Architecture, dan API Design Thinking.

---

# 📚 Materi yang Dipelajari

## Deep Work 1 — Cara Kerja Web & API

### HTTP (HyperText Transfer Protocol)

Memahami bagaimana Client dan Server berkomunikasi menggunakan mekanisme Request dan Response.

Topik:

* HTTP Request
* HTTP Response
* Header
* Body
* Status Code

---

### JSON

Memahami JSON sebagai format pertukaran data antara Client dan Server.

Contoh:

```json
{
  "id": 1,
  "name": "Naufalz"
}
```

---

### REST API

Mempelajari konsep:

* Resource
* Endpoint
* URI Design
* HTTP Method
* Stateless Architecture

Prinsip utama:

```text
URI = Noun
Method = Verb
```

Contoh:

```http
GET /users
POST /users
PATCH /users/1
DELETE /users/1
```

---

### HTTP Method

| Method | Fungsi         |
| ------ | -------------- |
| GET    | Read           |
| POST   | Create         |
| PUT    | Replace        |
| PATCH  | Partial Update |
| DELETE | Delete         |

---

### Path Parameter

Digunakan untuk mengakses resource spesifik.

Contoh:

```http
GET /users/10
```

---

### Query Parameter

Digunakan untuk filtering dan searching.

Contoh:

```http
GET /users?city=jakarta
```

---

### Status Code

| Status Code | Keterangan            |
| ----------- | --------------------- |
| 200         | OK                    |
| 201         | Created               |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 404         | Not Found             |
| 500         | Internal Server Error |

---

# 🧠 Deep Work 2

## Latihan A — Status Code Analysis

Menganalisis penggunaan status code pada berbagai skenario API.

Contoh:

* 400 Bad Request
* 401 Unauthorized
* 404 Not Found
* 500 Internal Server Error

---

## Latihan B — Idempotency Audit

Memahami konsep:

```text
Idempotent
=
Request yang dijalankan berkali-kali
tidak mengubah state akhir sistem
```

Contoh:

### Idempotent

```http
GET /reservations/15

DELETE /reservations/15

PATCH /reservations/15
{
  "status":"cancelled"
}
```

### Non-Idempotent

```http
POST /reservations
```

```http
PATCH /users/1
{
  "login_count": +1
}
```

---

## Latihan C — Error Response Design

Merancang struktur error response yang konsisten.

Contoh:

```json
{
  "error_code": "INVALID_DATE",
  "message": "Tanggal reservasi tidak valid",
  "details": {
    "field": "date"
  }
}
```

---

## Latihan D — API Design Thinking

Memahami perbedaan:

* Path Parameter
* Query Parameter
* Request Body

Contoh:

```http
GET /reservations/15
```

```http
GET /reservations?status=cancelled
```

```json
{
  "customer_name": "Naufalz",
  "guest_count": 4
}
```

---

## Latihan E — API Design Checklist

Checklist yang dipelajari:

* Resource menggunakan noun
* Collection Resource vs Single Resource
* API Versioning
* RESTful URI Design

Contoh:

```http
/v1/users
/v2/users
```

---

# 🎯 Hasil Pembelajaran

Setelah menyelesaikan Day 1, saya memahami:

✅ HTTP

✅ Request & Response

✅ JSON

✅ REST API

✅ Resource Design

✅ HTTP Method

✅ Path Parameter

✅ Query Parameter

✅ Status Code

✅ Idempotency

✅ Error Response Design

✅ API Versioning

---



# 🛠 Tech Stack

* Python
* REST API
* HTTP
* JSON
* FastAPI (Next Session)

---

# 👨‍💻 Author

**NaufalZ**


