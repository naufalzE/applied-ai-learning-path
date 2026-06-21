
"""
Deskripsi: ini digunakan untuk menyeleksi mahasiswa yang lulus dan gagal berdasarkan nilai yang diinputkan dengan ketentuan sama dengan 75 atau lebih dari.
Author: NaufalZ
"""
# Baris 1: variabel penampung lulus
mhs_lulus = 0
# Baris 2: variabel penampung gagal
mhs_gagal = 0
# Baris 3: mulai loop for sebanyak 5 kali
for i in range(5):
    nilai_mhs = int(input("masukkan nilai mahasiswa"))
    if nilai_mhs >= 75:
        mhs_lulus += 1
    else:
        mhs_gagal += 1
print("jumlah mahasiswa yang lulus: ", mhs_lulus)
print("jumlah mahasiswa yang gagal: ", mhs_gagal)