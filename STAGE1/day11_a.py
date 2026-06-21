import matplotlib.pyplot as plt
import numpy as np
bulan = np.array([
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "Mei"
])

user = np.array([
    100,
    150,
    200,
    250,
    320
])

plt.plot(bulan, user)
plt.xlabel("bulan")
plt.ylabel("user")
plt.title("Pertumbuhan User")
plt.show()


mata_kuliah = [
    "Algoritma",
    "Basis Data",
    "Jaringan",
    "AI"
]

jumlah_mahasiswa = [
    40,
    55,
    35,
    60
]

plt.bar(mata_kuliah,jumlah_mahasiswa)
plt.xlabel("matakuliah")
plt.ylabel("jumlah mahasiswa")
plt.title("Jumlah Mahasiswa per Mata Kuliah")
plt.show()

nilai_mahasiswa = [
    55, 60, 62, 65,
    70, 72, 75, 78,
    80, 82, 85, 88,
    90, 92, 95
]

plt.hist(
    nilai_mahasiswa,
    bins=10,
    edgecolor="black"
    )

plt.title("Distribusi Nilai Mahasiswa")

plt.xlabel("Nilai")

plt.ylabel("Frekuensi")

plt.show()

biaya_iklan = [
    100,
    200,
    300,
    400,
    500
]

penjualan = [
    1000,
    1500,
    2000,
    2600,
    3200
]

plt.scatter(biaya_iklan,penjualan)
plt.title("Hubungan Biaya Iklan dan Penjualan")
plt.xlabel("Biaya Iklan")

plt.ylabel("Penjualan")

plt.show()