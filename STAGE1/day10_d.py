import pandas as pd
import numpy as np

# 1. Load data asli kamu
file_path = "study_sessions.csv"
df = pd.read_csv(file_path)

# Pastikan data kosong sudah diisi rata-rata seperti modul sebelumnya
df["duration_minutes"] = df["duration_minutes"].fillna(df["duration_minutes"].mean())

print("--- STATISTIK AWAL (NORMAL) ---")
print(f"Mean awal: {df['duration_minutes'].mean():.2f}")
print(f"Median awal: {df['duration_minutes'].get('50%', df['duration_minutes'].median()):.2f}")

# 2. SIMULASI: Masukkan 'Outlier' (Misal: Kamu ketiduran pas ngoding, laptop nyala terus)
df_outlier = df.copy()
df_outlier.loc[0, "duration_minutes"] = 1440  # 1440 menit = 24 jam!

print("\n--- STATISTIK SETELAH ADA OUTLIER ---")
mean_bad = df_outlier["duration_minutes"].mean()
median_bad = df_outlier["duration_minutes"].median()
print(f"Mean baru: {mean_bad:.2f} (Melonjak jauh!)")
print(f"Median baru: {median_bad:.2f} (Tetap stabil!)")

# 3. DETEKSI OTOMATIS: Cari baris data yang mencurigakan (Right Skewed Check)
if mean_bad > median_bad * 1.5:  # Rule of thumb sederhana jika mean jauh di atas median
    print("\n⚠️ Peringatan: Terdeteksi Positive Outlier / Right Skewed Distribution!")
    
    # Ambil data yang durasinya di atas 3x median (pencilan ekstrem)
    cutoff = median_bad * 3
    outliers = df_outlier[df_outlier["duration_minutes"] > cutoff]
    print(f"Baris data yang terindikasi outlier (di atas {cutoff} menit):")
    print(outliers[["date", "topic", "duration_minutes"]])