# Stage 2 Day 3 - Virtual Environment & Package Management

## 📌 Overview

Pada Day 3 saya mempelajari konsep Virtual Environment, Package Management, PyPI, Requirements File, dan Dependency Reproducibility dalam ekosistem Python.

Materi ini penting karena hampir seluruh proyek AI Engineer, Backend Engineer, dan Data Engineer menggunakan banyak library eksternal yang harus dikelola dengan benar agar tidak terjadi konflik antar proyek.

---

# 🎯 Tujuan Pembelajaran

* Memahami alasan penggunaan Virtual Environment (venv)
* Memahami dependency conflict
* Memahami struktur internal Virtual Environment
* Memahami cara kerja activate
* Memahami fungsi pip sebagai package manager
* Memahami fungsi PyPI sebagai repository package Python
* Memahami requirements.txt
* Memahami pip freeze
* Memahami konsep reproducibility environment

---

# 📚 Materi yang Dipelajari

## 1. Virtual Environment (venv)

Virtual Environment adalah lingkungan Python terisolasi yang memungkinkan setiap proyek memiliki package dan dependency sendiri.

### Tanpa Virtual Environment

```text
Python Global
│
├── Project A
├── Project B
└── Project C
```

Semua proyek menggunakan package yang sama.

Risiko:

* Dependency conflict
* Sulit maintenance
* Sulit deployment

### Dengan Virtual Environment

```text
Project A
└── .venv

Project B
└── .venv

Project C
└── .venv
```

Setiap proyek memiliki package sendiri.

---

## 2. Dependency Conflict

Contoh:

Project A membutuhkan:

```text
requests==2.28.0
```

Project B membutuhkan:

```text
requests==2.34.2
```

Jika menggunakan Python Global, salah satu proyek berpotensi rusak karena versi package berbeda.

Solusi:

```text
Virtual Environment
```

---

## 3. Struktur Virtual Environment

```text
project/
│
├── app.py
│
└── venv/
    │
    ├── Scripts/
    ├── Lib/
    │   └── site-packages/
    └── pyvenv.cfg
```

### Scripts/

Berisi executable environment:

```text
python.exe
pip.exe
activate.bat
```

### site-packages/

Tempat seluruh package Python disimpan.

Contoh:

```text
requests/
urllib3/
certifi/
```

### pyvenv.cfg

Menyimpan konfigurasi environment.

Contoh:

```text
home = C:\Python313
include-system-site-packages = false
version = 3.14
```

---

## 4. Cara Kerja Activate

Perintah:

```bash
venv\Scripts\activate
```

Tidak membuat Python baru.

Activate hanya mengubah:

```text
PATH Environment Variable
```

Sehingga:

```bash
python
```

akan mengarah ke:

```text
venv\Scripts\python.exe
```

bukan Python Global.

---

## 5. pip

pip adalah Package Manager Python.

Fungsi:

* Download package
* Install package
* Upgrade package
* Mengelola dependency

Contoh:

```bash
pip install requests
```

---

## 6. PyPI

PyPI (Python Package Index) adalah repository resmi package Python.

Alur:

```text
Developer
    ↓
pip install requests
    ↓
PyPI
    ↓
Download Package
    ↓
site-packages
```

---

## 7. Dependency Resolution

Saat menjalankan:

```bash
pip install requests
```

Yang terinstall bukan hanya requests.

Tetapi juga dependency:

```text
requests
│
├── urllib3
├── certifi
├── idna
└── charset-normalizer
```

---

## 8. requirements.txt

File yang menyimpan daftar dependency proyek.

Contoh:

```text
requests==2.34.2
fastapi==0.120.0
uvicorn==0.38.0
```

Fungsi:

* Membagikan dependency ke developer lain
* Memastikan versi package sama
* Mendukung reproducibility

Install:

```bash
pip install -r requirements.txt
```

---

## 9. pip freeze

Menampilkan seluruh package yang terinstall dalam environment aktif.

Contoh:

```bash
pip freeze
```

Output:

```text
certifi==2026.6.17
charset-normalizer==3.4.7
idna==3.18
requests==2.34.2
urllib3==2.7.0
```

Membuat requirements.txt:

```bash
pip freeze > requirements.txt
```

---

# 🧪 Praktik yang Dilakukan

## Membuat Virtual Environment

```bash
python -m venv venv
```

## Aktivasi

```bash
venv\Scripts\activate.bat
```

## Install Requests

```bash
pip install requests
```

## Verifikasi Package

```bash
python -c "import requests; print(requests.__version__)"
```

Output:

```text
2.34.2
```

## Export Dependency

```bash
pip freeze > requirements.txt
```

---

# 🐞 Studi Kasus Debugging

Saya mengalami masalah ketika Virtual Environment tetap menggunakan interpreter dari project lama.

Gejala:

```text
(venv)
```

muncul tetapi:

```python
sys.prefix == sys.base_prefix
```

Masalah ditemukan pada:

```text
pyvenv.cfg
```

yang masih menunjuk ke environment project lain.

Solusi:

1. Hapus Virtual Environment lama
2. Buat ulang menggunakan:

```bash
python -m venv venv
```

3. Aktivasi ulang environment
4. Verifikasi menggunakan:

```bash
where python
```

dan

```python
import sys
print(sys.prefix)
print(sys.base_prefix)
```

Hasil:

```text
Virtual Environment Aktif
```

---

# 📊 IPO Workflow

| Input                         | Process                                   | Output                             |
| ----------------------------- | ----------------------------------------- | ---------------------------------- |
| python -m venv venv           | Membuat environment Python terisolasi     | Folder venv                        |
| venv\Scripts\activate         | Mengubah PATH ke interpreter venv         | Environment aktif                  |
| pip install requests          | Download package dan dependency dari PyPI | Package tersimpan di site-packages |
| pip freeze > requirements.txt | Membaca package pada environment aktif    | requirements.txt                   |

---

# 🎓 Kesimpulan

Virtual Environment merupakan fondasi penting dalam pengembangan software Python modern.

Dengan Virtual Environment:

* Dependency antar proyek tidak konflik
* Environment mudah direproduksi
* Deployment lebih aman
* Kolaborasi tim lebih mudah

Selain itu saya memahami bahwa Virtual Environment bersifat disposable, sehingga ketika terjadi kerusakan lebih baik membuat ulang environment daripada memperbaikinya secara manual.

---

## Progress Day 3

| Topik               | Pemahaman |
| ------------------- | --------- |
| Virtual Environment | 9/10      |
| Activate            | 9/10      |
| pip                 | 9/10      |
| PyPI                | 9/10      |
| requirements.txt    | 10/10     |
| pip freeze          | 9/10      |

**Status:** ✅ Completed
# 👨‍💻 Author

**NaufalZ**