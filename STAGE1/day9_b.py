# Total Durasi Semua Sesi

# Total Durasi Stage 1

# Rata-rata Durasi Semua Sesi

# Topik yang Muncul Paling Banyak

# Jumlah Sesi per Stage

import pandas as pd

data = pd.read_csv("study_sessions.csv")
print(data.head())
total_durasi = data["duration_minutes"].sum()
print("total durasi :",total_durasi)
stage1 = data[data["stage"] == "Stage 1"]
total_stage1 = stage1["duration_minutes"].sum()
print("total stage1     : ",total_stage1)
rata_rata = data["duration_minutes"].mean()
print(f"rata rata   : {rata_rata}")
count_value = data["topic"].value_counts()
print(f"topik paling banyak muncul  : {count_value}")
sesi = data["stage"].value_counts()
print(sesi)