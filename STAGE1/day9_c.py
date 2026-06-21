# Tantangan 1: Detektif Produktivitas (Filter Multi-Kondisi Sesi Pendek)
# •	Kasus: Kamu ingin mengevaluasi sesi belajar yang tidak efektif. Cari semua sesi belajar yang terjadi di Stage 1, tetapi memiliki durasi di bawah 30 menit. 
# •	Target Output: Tampilkan DataFrame berisi baris yang memenuhi syarat tersebut, lalu hitung ada berapa total sesi yang terbuang di bawah 30 menit.
# •	Poin Perhatian: Ingat aturan tanda kurung () untuk operator &.
# Tantangan 2: Audit Topik Spesifik (Seleksi & Agregasi)
# •	Kasus: Kamu ingin melihat seberapa intens kamu mendalami topik tertentu, misalnya "Pandas". Filter dataset hanya untuk baris yang kolom topic-nya bernilai "Pandas" atau "Python Basics". 
# •	Target Output: Hitung rata-rata durasi (mean) khusus untuk gabungan kedua topik tersebut.
# •	Poin Perhatian: Gunakan metode .isin(['Pandas', 'Python Basics']) untuk melakukan filter multi-nilai pada satu kolom secara efisien.
# Tantangan 3: Pencarian Berbasis Teks (String Handling pada Kolom)
# •	Kasus: Kadang kamu menulis nama topik secara variatif di CSV (misal: "OOP Dasar", "OOP Lanjutan"). Cari semua sesi yang kolom topic-nya mengandung kata "OOP", tidak peduli ada kata apa lagi di depan atau di belakangnya. 
# •	Target Output: Tampilkan daftar sesi uniknya dan hitung total durasinya.
# •	Poin Perhatian: Gunakan metode .str.contains('OOP', na=False) pada kolom topic.

import pandas as pd

data = pd.read_csv("study_sessions.csv")

kondisi = (data["stage"] == "Stage 1") & (data["duration_minutes"] < 30)
tidak_efektif = data[kondisi]
if tidak_efektif.empty:
    print("semua efektif")
else:
    print(tidak_efektif)
    jumlah_hari = len(tidak_efektif)
    print("jumlah hari tidak efektif    :",jumlah_hari)
    
kondisi_2 = data[data["topic"].isin(["Pandas","Python Basics"])]
mean_durasi = kondisi_2["duration_minutes"].mean()
print(kondisi_2)
print(f"rata rata waktu  : {mean_durasi} minutes")

mask_oop = data["topic"].str.contains("OOP",na=False)
final = data[mask_oop]

print(final)
print(sum(final["duration_minutes"]))