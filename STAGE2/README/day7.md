# 📘 Stage 2 - Day 7
# Python Logging & Production Logger

> Road to 100 Juta 🚀
>
> **Stage 2 - Deep Work 1 & Deep Work 2**
>
> Topik: **Python Logging Architecture & Production Logging**

---

# 🎯 Tujuan Pembelajaran

Setelah menyelesaikan Day 7, saya mampu:

- Memahami perbedaan Debugging dan Logging
- Memahami arsitektur internal Python Logging
- Membuat sistem logging tanpa `basicConfig()`
- Membuat logger production (`logger.py`)
- Menggunakan satu logger untuk seluruh project FastAPI
- Menggunakan multiple handler
- Menggunakan formatter
- Menggunakan file logging
- Menghindari duplicate handler

---

# Deep Work 1

## 1. Debugging vs Logging

### Debugging

Proses mencari penyebab bug.

Contoh:

```python
print(data)
```

Biasanya bersifat sementara.

---

### Logging

Mencatat aktivitas aplikasi.

Contoh:

```python
logger.info("Request Masuk")
```

Digunakan untuk:

- Monitoring
- Audit
- Debugging Production
- Maintenance

---

# Kenapa Tidak Menggunakan print()?

Karena print hanya menampilkan output.

Logging dapat:

- Memberikan level log
- Menentukan tujuan log
- Mengatur format
- Menyimpan ke file
- Mengirim ke cloud

---

# Arsitektur Logging

```
Program
    │
    ▼
Logger
    │
    ▼
Level Check
    │
    ▼
LogRecord
    │
    ▼
Filter
    │
    ▼
Handler
    │
    ▼
Formatter
    │
    ▼
Console / File
```

---

# Komponen Logging

## Logger

Tugas:

- menerima log
- mengecek level
- membuat LogRecord
- meneruskan ke Handler

---

## LogRecord

Menyimpan seluruh informasi log.

Contoh isi:

- levelname
- message
- filename
- module
- lineno
- funcName
- process
- threadName

---

## Filter

Menyaring log yang boleh diproses.

---

## Handler

Menentukan tujuan log.

Contoh:

- Console
- File
- Cloud
- Telegram

---

## Formatter

Menentukan tampilan log.

Contoh:

```
INFO | Halo Dunia
```

atau

```
2026-07-08 21:30:20 | INFO | main.py | Halo Dunia
```

---

# Logging Level

| Level | Nilai |
|--------|-------|
| DEBUG | 10 |
| INFO | 20 |
| WARNING | 30 |
| ERROR | 40 |
| CRITICAL | 50 |

Rule:

```
Log Level >= Config Level
```

---

# Deep Work 2

## Logging Dasar

```python
import logging

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(__name__)

logger.info("Halo Dunia")
```

Output

```
INFO:__main__:Halo Dunia
```

---

# Custom Formatter

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)
```

Output

```
INFO | Halo Dunia
```

---

# Manual Logging Configuration

```python
import logging

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(levelname)s | %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.INFO)

logger.info("Halo Dunia")
```

---

# Multiple Handler

```python
console_handler = logging.StreamHandler()

file_handler = logging.FileHandler("app.log")
```

Satu Logger

↓

Dua Handler

↓

Console + File

---

# File Logging

```python
file_handler = logging.FileHandler(
    "app.log"
)
```

Semua log otomatis disimpan ke:

```
app.log
```

---

# Reuse Formatter

```python
formatter = logging.Formatter(
    "%(levelname)s | %(message)s"
)

console_handler.setFormatter(formatter)

file_handler.setFormatter(formatter)
```

Satu Formatter

↓

Banyak Handler

---

# Production Logger

```
app/

├── core/
│     logger.py
│
├── routers/
├── services/
└── main.py
```

---

## logger.py

```python
import logging

logger = logging.getLogger("app")

if len(logger.handlers) == 0:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(levelname)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
```

---

# Penggunaan

Router

```python
from app.core.logger import logger

@router.post("/")
def translate(...):

    logger.info("Request Masuk")
```

---

Service

```python
from app.core.logger import logger

class TranslateService:

    def translate(...):

        logger.info("Translate Dimulai")
```

---

Main

```python
from app.core.logger import logger

logger.info("Server Berjalan")
```

---

# Posisi Logging yang Benar

✅ Import

```python
from app.core.logger import logger
```

Di atas file.

---

✅ Logging

Di dalam function.

```python
def translate():

    logger.info("Request Masuk")
```

---

❌ Hindari

```python
logger.info("Request Masuk")
```

di luar function karena akan dijalankan saat module di-import.

---

# Konsep OOP yang Digunakan

Logger

↓

Object

Handler

↓

Object

Formatter

↓

Object

Method yang dipelajari

- getLogger()
- setLevel()
- addHandler()
- setFormatter()
- info()

---

# Konsep API Design

| Method | Tujuan |
|----------|---------|
| get | Mengambil |
| set | Mengganti nilai |
| add | Menambahkan ke koleksi |

Contoh

```python
logger.addHandler(handler)
```

Karena Logger memiliki banyak Handler.

Sedangkan

```python
handler.setFormatter(formatter)
```

Karena satu Handler hanya menggunakan satu Formatter.

---

# Konsep Penting

- Logger membuat LogRecord.
- Handler menentukan tujuan log.
- Formatter menentukan tampilan log.
- Filter menyaring log.
- Logger dapat memiliki banyak Handler.
- Formatter dapat digunakan kembali (reuse).
- Semua file menggunakan satu logger yang sama.

---

# Hasil Akhir

Saya berhasil membuat sistem logging production sederhana yang terdiri dari:

- Logger
- StreamHandler
- FileHandler
- Formatter
- Multiple Handler
- logger.py
- Integrasi FastAPI

---

# Yang Saya Pelajari Hari Ini

✅ Logging bukan pengganti print().

✅ Logger hanya membuat LogRecord.

✅ Handler menentukan tujuan log.

✅ Formatter hanya mengubah tampilan.

✅ Logging mengikuti prinsip Single Responsibility Principle (SRP).

✅ Logger dapat memiliki banyak Handler.

✅ Satu Formatter dapat digunakan oleh banyak Handler.

✅ Logging production menggunakan satu file konfigurasi (`logger.py`) yang digunakan di seluruh project.

---

# Progress

```
Road to 100 Juta

Stage 2

Day 1 ✅
Day 2 ✅
Day 3 ✅
Day 4 ✅
Day 5 ✅
Day 6 ✅
Day 7 ✅
```

---

# Mentor Assessment

**Pemahaman:** ⭐⭐⭐⭐⭐ (9.9/10)

Hari ini saya berhasil memahami bukan hanya cara menggunakan Python Logging, tetapi juga arsitektur internalnya, hubungan antar komponen, serta implementasi logger production yang siap digunakan pada project FastAPI.