# 📝 Skenario Kasus:
# Kamu baru saja mengekstrak data histori belajar dari sistem log lokal. Namun, karena ada kegagalan sinkronisasi API pada beberapa hari, ada beberapa data durasi yang kosong (NaN). Selain itu, pada baris pertama, sistem mencatat angka 1440 menit karena laptopmu lupa dimatikan dalam posisi program berjalan.

# 🛠️ Tugas Kamu (Tulis Kode Python):
# Load & Kontaminasi Data:

# Load file study_sessions.csv.

# Buat DataFrame replika bernama df_audit menggunakan .copy() agar data asli tidak rusak.

# Masukkan data outlier secara sengaja: ubah baris indeks ke-0 pada kolom duration_minutes menjadi 1440.

# Handling Missing Values (Imputasi Robust):

# Hitung berapa total data kosong di kolom duration_minutes.

# Karena data kamu sekarang punya outlier raksasa (1440), jangan gunakan Mean untuk mengisi data kosong karena nilainya sudah rusak.

# Tugas: Isi (fillna) data kosong di kolom duration_minutes menggunakan nilai Median dari kolom tersebut.

# Grouping & Agregasi Otomatis:

# Hitung rata-rata durasi belajar per Topik (topic) menggunakan kombinasi .groupby() dan .mean().

# Gunakan .reset_index() di akhir agar outputnya tetap berupa DataFrame tabular yang rapi.

# Uji Detektor Outlier Otomatis:

# Buat kondisi if-else untuk mengecek apakah Mean dari df_audit["duration_minutes"] sudah lebih besar dari Median * 1.5.

# Jika True, cetak kalimat: "⚠️ Bahaya: Data Naufalz terindikasi Right Skewed karena Outlier!".

# Jika False, cetak kalimat: "✅ Data aman dan berdistribusi normal."

import pandas as pd
df = pd.read_csv("study_sessions.csv")

df_audit = df.copy()
df_audit.loc[0,"duration_minutes"] = 1440

input_fil = df_audit["duration_minutes"].median()
total_missing = df_audit["duration_minutes"].isna().sum()
if total_missing == 0:
    print("data aman tidak ada NaN")
else:
    df_audit["duration_minutes"] = df_audit["duration_minutes"].fillna(input_fil)
    print("total missing    : ",total_missing)

durasi_pertopic = df_audit.groupby("topic")["duration_minutes"].mean().reset_index()
print("\n--- Rata-rata Durasi Per Topik ---")
print(durasi_pertopic)

mean1 = df_audit["duration_minutes"].mean()
median1 = df_audit["duration_minutes"].median()

if mean1 > median1 * 1.5:
    print("⚠️ Bahaya: Data Naufalz terindikasi Right Skewed karena Outlier!")
else:
    print("✅ Data aman dan berdistribusi normal.")